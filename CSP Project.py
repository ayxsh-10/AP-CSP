#Imports
import pygame
import sys
import math

pygame.init()

#-----Global-Variables----
width, height = 800, 600
fps = 60

#Fonts
font_title  = pygame.font.Font(None, 48)  #for menu title
font_button = pygame.font.Font(None, 28)  #for button labels
font_score  = pygame.font.Font(None, 24)  #for scores and rings
font_small  = pygame.font.Font(None, 18)  #for small hints

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Skeeball w/ PyGame")
clock = pygame.time.Clock()

#Colors
bg_color = (10, 10, 20)
lane_color = (120, 80, 40)
ring_color = (200, 200, 200)
ball_color = (230, 230, 80)
guide_color = (100, 200, 255)
button_bg = (60, 60, 60)
button_hover = (100, 100, 100)
overlay_bg = (20, 20, 30)
overlay_border = (200, 0, 200)

#Physics
gravity = 0.4
friction_x = 0.95
bounce_damp = 0.5
power_scale = 0.18

#Ball and lane setup
start_x = width // 2
start_y = height - 80
ball_radius = 12
ball_x = start_x
ball_y = start_y
ball_vx = 0
ball_vy = 0
ball_in_air = False
ball_at_rest = True

lane_top = 80
lane_margin = 100
lane_bottom = height - 10

#Game state
score_total = 0
shots = 0
shot_scores = []
state = "menu"
show_rules = False
show_score_overlay = False
dragging = False
mouse_pos = (0, 0)

#Buttons
menu_buttons = []
game_buttons = []

#Scoring Rings
rings = [
    (width // 2, lane_top + 40, 22, 100),
    (width // 2 - 90, lane_top + 70, 35, 100),
    (width // 2 + 90, lane_top + 70, 35, 100),
    (width // 2, lane_top + 125, 50, 40),
    (width // 2, lane_top + 200, 80, 10),
]

#-----Button-Class----
class Button:
    def __init__(self, x, y, w, h, on_click=None, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.on_click = on_click
        self.text = text
        self.font = font_button

    def draw(self, surface):
        mouse_pos_local = pygame.mouse.get_pos()
        color = button_hover if self.rect.collidepoint(mouse_pos_local) else button_bg
        pygame.draw.rect(surface, color, self.rect, border_radius=8)


        if self.text:
            txt_surf = self.font.render(self.text, True, (255,255,255))
            txt_rect = txt_surf.get_rect(center=self.rect.center)
            surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.on_click:
                self.on_click()

#-----Game-Logic----
def reset_ball():
    global ball_x, ball_y, ball_vx, ball_vy, ball_in_air, ball_at_rest
    ball_x = start_x
    ball_y = start_y
    ball_vx = 0
    ball_vy = 0
    ball_in_air = False
    ball_at_rest = True

def full_reset():
    global score_total, shots, shot_scores
    reset_ball()
    score_total = 0
    shots = 0
    shot_scores = []

def launch_ball(pos):
    global ball_vx, ball_vy, ball_in_air, ball_at_rest, shots
    mx, my = pos
    dx = ball_x - mx
    dy = ball_y - my
    ball_vx = dx * power_scale
    ball_vy = dy * power_scale
    ball_in_air = True
    ball_at_rest = False
    shots += 1

def update_ball():
    global ball_x, ball_y, ball_vx, ball_vy, ball_in_air, ball_at_rest, score_total, shot_scores
    if not ball_in_air:
        return

    ball_vy += gravity
    ball_x += ball_vx
    ball_y += ball_vy

    if ball_x - ball_radius < lane_margin:
        ball_x = lane_margin + ball_radius
        ball_vx = -ball_vx * 0.8
    if ball_x + ball_radius > width - lane_margin:
        ball_x = width - lane_margin - ball_radius
        ball_vx = -ball_vx * 0.8

    if ball_y + ball_radius > height - 10:
        ball_y = height - 10 - ball_radius
        ball_vy = -ball_vy * bounce_damp
        ball_vx *= friction_x

    speed = math.hypot(ball_vx, ball_vy)
    if speed < 0.3 and ball_y < lane_top + 260:
        ball_in_air = False
        ball_at_rest = True
        ball_vx = 0
        ball_vy = 0
        pts = compute_score()
        score_total += pts
        shot_scores.append(pts)

def compute_score():
    best = 0
    for cx, cy, r, pts in rings:
        if math.hypot(ball_x - cx, ball_y - cy) <= r:
            best = max(best, pts)
    return best

#-----Drawing----
def draw_lane():
    pygame.draw.rect(screen, lane_color, (lane_margin, lane_top, width - 2*lane_margin, height - lane_top), border_radius=30)

def draw_rings():
    for cx, cy, r, pts in rings:
        pygame.draw.circle(screen, ring_color, (cx, cy), r, 3)
        #label each ring with its points, using font_score
        txt = font_score.render(str(pts), True, (255, 255, 255))
        txt_rect = txt.get_rect(center=(cx, cy))
        screen.blit(txt, txt_rect)

def draw_ball():
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

def draw_menu():
    screen.fill(bg_color)

    #title line 1
    title_surf = font_title.render("SKEEBALL", True, (255, 255, 255))
    title_rect = title_surf.get_rect(center=(width // 2, height // 3 - 30))
    screen.blit(title_surf, title_rect)

    #title line 2
    subtitle_surf = font_title.render("IN PYGAME", True, (255, 255, 255))
    subtitle_rect = subtitle_surf.get_rect(center=(width // 2, height // 3 + 30))
    screen.blit(subtitle_surf, subtitle_rect)

    for b in menu_buttons:
        b.draw(screen)

    if show_rules:
        draw_rules_overlay()
    
def draw_rules_overlay():
    overlay_rect = pygame.Rect(width // 2 - 260, height // 2 - 150, 520, 300)
    pygame.draw.rect(screen, overlay_bg, overlay_rect)
    pygame.draw.rect(screen, overlay_border, overlay_rect, 2)

    rules_title = font_score.render("RULES", True, (255, 255, 255))
    screen.blit(rules_title, (overlay_rect.x + 20, overlay_rect.y + 15))

    #Rules of Game Defined:
    rules = [
        "Drag ball to aim and set power",
        "Release mouse to launch", 
        "Ball stops in ring = points",
        "Each shot tracked in score table",
        "Click Score button to view"
    ]
    
    for i, rule in enumerate(rules):
        txt = font_small.render(rule, True, (255, 255, 255))
        screen.blit(txt, (overlay_rect.x + 20, overlay_rect.y + 50 + i * 25))

def draw_game_hud():
    title = font_score.render("SKEEBALL", True, (255, 255, 255))
    screen.blit(title, (width // 2 - title.get_width() // 2, 15))
    
    total_txt = font_score.render(f"Score: {score_total}", True, (255, 255, 255))
    shots_txt = font_score.render(f"Shots: {shots}", True, (255, 255, 255))
    screen.blit(total_txt, (width - total_txt.get_width() - 15, 15))
    screen.blit(shots_txt, (width - shots_txt.get_width() - 15, 40))

def draw_score_overlay():
    overlay_rect = pygame.Rect(width // 2 - 260, height // 2 - 150, 520, 300)
    pygame.draw.rect(screen, overlay_bg, overlay_rect)
    pygame.draw.rect(screen, overlay_border, overlay_rect, 2)

    header = font_score.render("SHOT SCORES", True, (255, 255, 255))
    screen.blit(header, (overlay_rect.centerx - header.get_width() // 2, overlay_rect.y + 20))

    for i, pts in enumerate(shot_scores[-8:], start=max(1, len(shot_scores)-7)):
        row = font_small.render(f"Shot {i}: {pts} pts", True, (255, 255, 255))
        screen.blit(row, (overlay_rect.x + 30, overlay_rect.y + 70 + (i-1)*28))
    
    total = font_score.render(f"TOTAL: {score_total}", True, (255, 255, 255))
    screen.blit(total, (overlay_rect.centerx - total.get_width() // 2, overlay_rect.bottom - 45))


    #Draw title
    title_surf = font_title.render("SKEEBALL", True, (255,255,255))
    title_rect = title_surf.get_rect(center=(width // 2, height // 3))
    screen.blit(title_surf, title_rect)
    
    #Draw buttons
    for b in menu_buttons:
        b.draw(screen)

#-----Main-Loop----
def main():
    global state, show_score_overlay, menu_buttons, game_buttons, dragging, mouse_pos

    running = True

    #-----Button-Callbacks----
    def start_game():
        global state, dragging
        dragging = False
        state = "game"

    def quit_game():
        pygame.quit()
        sys.exit()

    def toggle_score():
        global show_score_overlay
        show_score_overlay = not show_score_overlay

    def toggle_rules():
        global show_rules
        show_rules = not show_rules

    def back_to_menu():
        global state, show_score_overlay
        state = "menu"
        show_score_overlay = False
        reset_ball()


    def reset_game():
        full_reset()

    #-----Initialize-Buttons----
    menu_buttons[:] = [
        Button(width // 2 - 100, height // 2 + 40, 200, 45, start_game, text="Play"),
        Button(width // 2 - 100, height // 2 + 100, 200, 45, toggle_rules, text="Rules"),
        Button(width // 2 - 100, height // 2 + 160, 200, 45, quit_game, text="Quit"),
    ]

    game_buttons[:] = [
        Button(15, height - 50, 100, 35, toggle_score, "Score"),
        Button(125, height - 50, 100, 35, reset_game, "Reset"),
        Button(width - 230, height - 50, 100, 35, back_to_menu, "Menu"),
        Button(width - 120, height - 50, 100, 35, quit_game, "Quit"),
    ]

    #-----Main-Game-Loop----
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if state == "menu":
                for b in menu_buttons:
                    b.handle_event(event)
            
            elif state == "game":
                for b in game_buttons:
                    b.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if ball_at_rest:
                        if math.hypot(mouse_pos[0]-ball_x, mouse_pos[1]-ball_y) <= ball_radius+10:
                            dragging = True

                elif event.type == pygame.MOUSEBUTTONUP and dragging:
                    dragging = False
                    launch_ball(event.pos)

        #-----Drawing----
        screen.fill(bg_color)

        if state == "menu":
            draw_menu()

        else:
            update_ball()
            draw_lane()
            draw_rings()
            draw_ball()
            draw_game_hud()
            for b in game_buttons:
                b.draw(screen)
            if dragging:
                pygame.draw.line(screen, guide_color, (ball_x, ball_y), mouse_pos, 2)
            if show_score_overlay:
                draw_score_overlay()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

#-----Run-Game----
if __name__ == "__main__":
    full_reset()
    main()

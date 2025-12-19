#imports
import pygame
import sys
import math

pygame.init()

def some_function():
    global dragging, mouse_pos
    dragging = True
    mouse_pos = pygame.mouse.get_pos()

menu_buttons = []
game_buttons = []

#Global Variables Setup
width, height = 800, 600
fps = 60

screen = pygame.display.set_mode(width, height)
pygame.display.set_caption("Skeeball w/ PyGame")
clock = pygame.time.Clock()

#Colors
bg_color = (10,10,20)
lane_color = (120,80,40)
ring_color = (200,200,200)
ball_color = (230,230,80)
guide_color = (100,200,255)
button_bg = (60,60,60)
button_hover = (100,100,100)
overlay_bg = (20,20,30)
overlay_border = (200,0,200)

#Physics
gravity = 0.4
friction_x = 0.95
bounce_damp =0.5
power_scale = 0.18

#Initial Positions
start_x = width // 2
start_y = height - 80

#Ball Position
ball_radius = 12
ball_x = start_x
ball_y = start_y

#Ball Initial Velocities
ball_vx = 0
ball_vy = 0

#Ball Conditions
ball_in_air = False
ball_at_rest = True

#Lane Dimensions
lane_top = 80
lane_margin = 100
lane_bottom = height - 10

#Game Initials
score_total = 0
shots = 0
shot_scores = []
state = "menu"
show_rules = False
show_score_overlay = False

#Scoring Rings
rings = [
    #basic formulas: (center_x. center_y, radius, points)
    (width // 2, lane_top + 40, 22, 100),
    (width // 2 - 90, lane_top + 70, 35, 100),
    (width // 2 + 90, lane_top + 70, 35, 100),
    (width // 2, lane_top + 125, 50, 40),
    (width // 2, lane_top + 200, 80, 10),
]

#Button Class
class Button:
    def __init__(self, x, y, w, h, on_click=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.on_click = on_click
    
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = button_hover if self.rect.collidepoint(mouse_pos) else button_bg
        pygame.draw.rect(surface, color, self.rect, border_radius=8)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.on_click:
                self.on_click()

#Game Logic
def reset_ball():
    global ball_x, ball_y, ball_vx, ball_vy, ball_in_air, ball_at_rest
    ball_x = start_x
    ball_x = start_x
    ball_y = start_y
    ball_vx = 0
    ball_vy = 0
    ball_in_air = False
    ball_at_rest = True

def full_reset():
    reset_ball()
    score_total = 0
    shots = 0
    shot_scores = []

def launch_ball(mouse_pos):
    global ball_vx, ball_vy, ball_in_air, ball_at_rest, shots
    mx, my = mouse_pos
    dx = ball_x - mx
    dy = ball_y - my
    power = 0.18
    ball_vx = dx * power
    ball_vy = dy * power
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

    lane_margin = 100
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
        ball_vx = ball_vy = 0
        pts = compute_score()
        score_total += pts
        shot_scores.append(pts)

def compute_score():
    best = 0
    for cx, cy, r, pts in rings:
        if math.hypot(ball_x - cx, ball_y - cy) <= r:
            best = max(best, pts)
    return best

#Drawing Objects
def draw_lane():
    margin = 100
    pygame.draw.rect(
        screen, lane_color,
        (margin, lane_top, width - 2 * margin, height - lane_top),
        border_radius = 30
    )

def draw_rings():
    for cx, cy, r, _ in rings:
        pygame.draw.circle(screen,ring_color,(cx, cy), r, 3)

def draw_ball():
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

#Main Loop
def main():
    global state, show_score_overlay

    running = True
    dragging = False

    def start_game():
        nonlocal dragging
        dragging = False
        globals()["state"] = "game"

    def quit_game():
        pygame.quit()
        sys.exit()
    
    def toggle_score():
        globals()["show_score_overlay"] = not globals()["show_score_overlay"]

    def back_to_menu():
        globals()["state"] = "menu"
        globals()["show_score_overlay"] = False

    def reset_game():
        full_reset()

    menu_buttons = [
        Button(width//2 - 100, height//2 + 40, 200, 45, start_game),
        Button(width//2 - 100, height//2 + 100, 200, 45, quit_game),
    ]

    game_buttons = [
        Button(15, height - 50, 100, 35, toggle_score),
        Button(125, height - 50, 100, 35, reset_game),
        Button(width - 230, height - 50, 100, 35, back_to_menu),
        Button(width - 120, height - 50, 100, 35, quit_game),
    ]

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False\
        
            if state == "menu":
                for b in menu_buttons:
                    b.handle_event(event)
            
            elif state == "game":
                for b in game_buttons:
                    b.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if ball_at_rest:
                        if math.hypot(mouse_pos[0] - ball_x, mouse_pos[1] - ball_y) <= ball_radius + 10:
                            dragging = True

                elif event.type == pygame.MOUSEBUTTONUP and dragging:
                    dragging = False
                    launch_ball(event.pos)

screen.fill(bg_color)

if state == "menu":
    for b in menu_buttons:
        b.draw(screen)

else:
    update_ball()
    draw_lane()
    draw_rings()
    draw_ball()
    for b in game_buttons:
        b.draw(screen)
    if dragging:
        pygame.draw.line(screen, guide_color, (ball_x, ball_y), mouse_pos, 2)

pygame.display.flip()
clock.tick(fps)

pygame.quit()
sys.exit()

if __name__ == "__main__":
    full_reset()
    main()

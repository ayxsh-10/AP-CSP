#
import pygame
import random
import math
import sys

pygame.init()
WIDTH, HEIGHT = 400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

score = 0
current_strength = 5
hole_scores = [10, 20, 30, 40, 50, 100]
holes_x = [75, 150, 225]
hole_y = 60
hole_radius = 20

last_hole_index = None

def roll_ball(strength: int) -> int:

    r = random.random() * 10

    if strength <= 2:
        return 0 if r < 8 else 1
    elif strength <= 4:
        if r < 2:
            return 0
        elif r < 8:
            return 1
        else:
            return 2
        
GREEN = (46, 125, 50)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

def draw_lane():
    screen.fill(GREEN)
    for x in holes_x:
        pygame.draw.circle(screen, WHITE, (x, hole_y), hole_radius)
        pygame.draw.circle(screen, BLACK, (x, hole_y), hole_radius, 2)

def draw_ball():
    if last_hole_index is not None:
        x = hole_y[last_hole_index]
        y = hole_y + 60
        pygame.draw.circle(screen, WHITE, (x, y), 10)
        pygame.draw.circle(screen, BLACK, (x, y), 10, 2)

def draw_ui():
    strength_text = font.render(f"Strength: {current_strength}", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    instr_text = font.render("1-5 = strength, SPACE = roll", True, WHITE)

    screen.blit(strength_text, (10, HEIGHT - 70))
    screen.blit(score_text, (10, HEIGHT - 50))
    screen.blit(instr_text, (10, HEIGHT - 30))

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
        pygame.display.update()

pygame.quit()


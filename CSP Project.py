#imports
import pygame
import sys
import math

pygame.init()

#Global Variables Setup
WIDTH, HEIGHT = 800, 600
LANE_TOP = 80
FPS = 60

screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_title("Skeeball w/ PyGame")
clock = pygame.time.Clock()

#Colors
BG_COLOR = (10,10,20)
LANE_COLOR = (120,80,40)
RING_COLOR = (200,200,200)
BALL_COLOR = (230,230,80)
GUIDE_COLOR = (100,200,255)
BUTTON_BG = (60,60,60)
BUTTON_HOVER = (100,100,100)
OVERLAY_BG = (20,20,30)
OVERLAY_BORDER = (200,200,200)

#Physics
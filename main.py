# importing modules
import pygame
import os
import time
import random

WIDTH, HEIGHT = 750,750
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")

# loading images
RED_SHIP = pygame.image.load("assets\pixel_ship_red_small.png")
GREEN_SHIP = pygame.image.load("assets\pixel_ship_green_small.png")
BLUE_SHIP = pygame.image.load("assets\pixel_ship_blue_small.png")

# player ship
YELLOW_SHIP = pygame.image.load("assets\pixel_ship_yellow.png")

# lasers
RED_LASER = pygame.image.load("assets\pixel_laser_red.png")
GREEN_LASER = pygame.image.load("assets\pixel_laser_green.png")
BLUE_LASER = pygame.image.load("assets\pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("assets\pixel_laser_yellow.png")

#background image 
BACKGROUND_IMG = pygame.image.load(os.path.join("assets","background-black.png"))
# Ben Nesbit
# power_up.py

# import pygame module
import pygame

POWER_UP_WIDTH = 55
POWER_UP_HEIGHT = 100

IMAGE_POWER_UP_BOMB = \
    pygame.transform.scale(pygame.image.load('images/bomb_power_up.png'), \
        (POWER_UP_WIDTH, POWER_UP_HEIGHT))
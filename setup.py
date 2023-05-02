import pygame
import constants.static
pygame.init()
screen = pygame.display.set_mode(
    (constants.static.WIDTH, constants.static.HEIGHT))
pygame.display.set_caption("Attack on Planet Earth")
clock = pygame.time.Clock()
running = 1

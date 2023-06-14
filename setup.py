import pygame
import constant.static
pygame.init()
screen = pygame.display.set_mode(
    (constant.static.WIDTH, constant.static.HEIGHT))
pygame.display.set_caption("Attack on Planet Earth")
clock = pygame.time.Clock()
running = True
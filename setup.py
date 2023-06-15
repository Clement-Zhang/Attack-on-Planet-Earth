import pygame
import data.constant
pygame.init()
screen = pygame.display.set_mode(
    (data.constant.WIDTH, data.constant.HEIGHT))
pygame.display.set_caption("Attack on Planet Earth")
clock = pygame.time.Clock()
running = True
import pygame
import constants.static
pygame.init()
screen = pygame.display.set_mode((constants.static.WIDTH, constants.static.HEIGHT))
pygame.display.set_caption("Extra Space Invaders")
clock = pygame.time.Clock()
running = 1
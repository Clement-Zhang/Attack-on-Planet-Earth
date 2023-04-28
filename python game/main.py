import pygame
import random

import constants
from player import Player
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Extra Space Invaders")
clock = pygame.time.Clock()
running = 1

all = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

Player(players,all)
for i in range(random.randrange(1, 10)):
    Enemy(players,all,enemies)

while running:
    clock.tick(constants.FPS)
    # process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    # update
    all.update()
    # draw screen
    screen.fill(constants.BACKGROUND)
    all.draw(screen)
    pygame.display.flip()
pygame.quit

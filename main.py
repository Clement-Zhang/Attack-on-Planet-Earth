import pygame
import random
from constants import static

pygame.init()
screen = pygame.display.set_mode((static.WIDTH, static.HEIGHT))
pygame.display.set_caption("Extra Space Invaders")
clock = pygame.time.Clock()
running = 1

import constants
from player import Player
from enemy import Enemy

all = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

Player(players,all)
for i in range(random.randrange(1, 10)):
    Enemy(players,all,enemies)

while running:
    clock.tick(constants.static.FPS)
    # process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = 0
    # update
    all.update()
    # draw screen
    screen.fill(constants.static.BACKGROUND)
    all.draw(screen)
    pygame.display.flip()
pygame.quit

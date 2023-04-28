import pygame
import random
import os
import math


WIDTH = 1280
HEIGHT = 720
FPS = 30
BACKGROUND = (0, 0, 0)

game_folder = os.path.dirname(__file__)
player_folder = os.path.join(
    game_folder, "PlatformerArtCompletePack\Basepack\Player")
enemy_folder = os.path.join(
    game_folder, "PlatformerArtCompletePack\Basepack\Enemies")


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Player(Entity):
    def __init__(self, *sprite_groups):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def move(self):
        start = self.rect.center
        end = pygame.mouse.get_pos()
        dist_x = end[0]-start[0]
        dist_y = -(end[1]-start[1])
        pi = math.pi
        if dist_x == 0:
            dist_x = 10 ** -6
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle)*(hypot/2)**.5
        y = -math.sin(angle)*(hypot/2)**.5
        if abs(hypot*math.cos(angle)) < 5:
            x = 0  # center
        if x > 5 and angle < (.5*pi) and angle > (-.5*pi):
            x = 5  # right
        if x < -5 and angle < (-.5*pi) or angle > (.5*pi):
            x = -5  # left
        if abs(hypot*math.sin(angle)) < 5:
            y = 0  # center
        if y > 5 and angle < 0:
            y = 5  # down
        if y < -5 and angle > 0:
            y = -5  # up
        self.rect.centerx += x
        self.rect.centery += y

    def update(self):
        self.move()


class Enemy(Entity):
    def __init__(self, players, *sprite_groups):
        super().__init__()
        self.players = players
        self.image = enemy_block_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(25, WIDTH-25)
        self.rect.centery = random.randrange(25, HEIGHT-25)
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def move(self):
        possible_targets = self.players.sprites()
        target = possible_targets[0]
        target_dist = math.hypot(
            target.rect.centerx-self.rect.centerx, target.rect.centery-self.rect.centery)
        for i in range(1, len(possible_targets)):
            dist = math.hypot(possible_targets[i].rect.centerx-self.rect.centerx,
                              possible_targets[i].rect.centery-self.rect.centery)
            if dist < target_dist:
                target_dist = dist
                target = possible_targets[i]
        start = self.rect.center
        end = target.rect.center
        dist_x = end[0]-start[0]
        dist_y = end[1]-start[1]
        hypot = math.hypot(dist_x, dist_y)
        if hypot == 0:
            hypot = 10**-6
        unit_x = dist_x/hypot
        unit_y = dist_y/hypot
        self.rect.centerx += unit_x*4
        self.rect.centery += unit_y*4
    def update(self):
        self.move()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_img = pygame.image.load(os.path.join(
    player_folder, "p1_stand.png")).convert()
enemy_block_img = pygame.image.load(os.path.join(
    enemy_folder, "blockerBody.png")).convert()
enemy_block_img = pygame.transform.scale(enemy_block_img, (25, 25))
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
    clock.tick(FPS)
    # process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    # update
    all.update()
    # draw screen
    screen.fill(BACKGROUND)
    all.draw(screen)
    pygame.display.flip()
pygame.quit

import os
import pygame
import constants.static

GAME_FOLDER = os.path.join(os.path.dirname(__file__), '..')
PLAYER_FOLDER = os.path.join(
    GAME_FOLDER, "custom art/player")
ENEMY_FOLDER = os.path.join(
    GAME_FOLDER, "custom art/enemy")
PLAYER_IMG = pygame.image.load(os.path.join(
    PLAYER_FOLDER, "basic plane.png")).convert()
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (constants.static.SPRITE_SIZE, constants.static.SPRITE_SIZE))
ENEMY_IMG = pygame.image.load(os.path.join(
    ENEMY_FOLDER, "basic plane.png")).convert()
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (constants.static.SPRITE_SIZE, constants.static.SPRITE_SIZE))

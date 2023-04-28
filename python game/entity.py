import pygame
import os

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update():
        pass

game_folder = os.path.dirname(__file__)
player_folder = os.path.join(
    game_folder, "PlatformerArtCompletePack\Basepack\Player")
enemy_folder = os.path.join(
    game_folder, "PlatformerArtCompletePack\Basepack\Enemies")
player_img = pygame.image.load(os.path.join(
    player_folder, "p1_stand.png")).convert()
enemy_block_img = pygame.image.load(os.path.join(
    enemy_folder, "blockerBody.png")).convert()
enemy_block_img = pygame.transform.scale(enemy_block_img, (25, 25))
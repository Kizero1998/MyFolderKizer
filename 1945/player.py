import pygame
from inputmanager import *
from gamemanager import *
from player_bullet import *
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load_basic("Resource/player.png")
        self.input_manager = None
    def draw(self, screen):
        screen.blit(self.image, (self.x-self.image.get_width()/2, self.y-self.image.get_height()/2))
    def run(self):
        if self.input_manager is not None:
            if self.input_manager.right_pressed:
                self.x += 3
            if self.input_manager.left_pressed:
                self.x -= 3
            if self.input_manager.down_pressed:
                self.y += 3
            if self.input_manager.up_pressed:
                self.y -= 3
            if input_manager.space_pressed:
                player_bullet = PlayerBullet()
                player_bullet.x = self.x
                player_bullet.y = self.y
                game_manager.add(player_bullet)
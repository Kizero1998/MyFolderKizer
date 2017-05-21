import pygame
class PlayerBullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image.load("resource/player-bullet.png")
    def run(self):
        self.y -=10
    def draw(self, screen):
        screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))
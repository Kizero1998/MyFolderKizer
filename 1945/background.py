import pygame
class Background:
    def __init__(self):
        self.imgage = pygame.image.load("Resource/background.png")
        self.y = 0
        self.y2 = -self.imgage.get_height()
    def draw(self,screen):
        screen.blit(self.imgage, (0, self.y))
        screen.blit(self.imgage, (0, self.y2))
    def run(self):
        pass
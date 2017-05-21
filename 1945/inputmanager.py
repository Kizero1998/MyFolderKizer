import pygame

class inputmanager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False

    def run(self, events):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                elif event.key == pygame.K_LEFT:
                    self.right_pressed = True
                elif event.key == pygame.K_UP:
                    self.right_pressed = True
                elif event.key == pygame.K_DOWN:
                    self.right_pressed = True
                elif event.key == pygame.K_SPACE:
                    self.right_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                elif event.key == pygame.K_LEFT:
                    self.right_pressed = False
                elif event.key == pygame.K_UP:
                    self.right_pressed = False
                elif event.key == pygame.K_DOWN:
                    self.right_pressed = False
                elif event.key == pygame.K_SPACE:
                    self.right_pressed = False

input_manager = inputmanager()
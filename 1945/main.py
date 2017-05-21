import pygame
from player import *
from inputmanager import *
from background import *
from gamemanager import *
loop = True

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("1945 striker")
    return screen

def handel_exit_event(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True

def run():
    game_manager.run()


def draw(screen):
    screen.fill((0,0,0))
    game_manager.draw(screen)
init_pygame()

screen = init_pygame()

clock = pygame.time.Clock()
game_manager.add(Player())
game_manager.add(Background())
loop = True



while loop:
    events = pygame.event.get()
    loop = handel_exit_event(events)

    for event in events:
        if event.type == pygame.QUIT:
            loop=False
    input_manager.run(events)
    run()

    draw(screen)
    #delay by framerate
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
import pygame
import os

import walls as walls

pygame.init()
pygame.display.set_caption("Sokoban")
screen = pygame.display.set_mode((600,400))

loop = True

clock = pygame.time.Clock()

time = 0

mario_image = pygame.image.load("mario.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("box.png")
mario_x=0
mario_y=0
mario_col =0
mario_row =0
next_mario_row = 0
next_mario_col = 0
box_row = 5
box_col = 5
#moveps=1
square_width = square_image.get_width()
square_height = square_image.get_height()

col_count = 5
row_count = 5

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False

class Mario(object):
    def __init__(self):
        self.rect = pygame.Rect(mario_image)

        def move(self, dx, dy):

            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)

        def move_single_axis(self, dx, dy):

            # Move the rect
            self.rect.x += dx
            self.rect.y += dy

            # If you collide with a wall, move out based on velocity
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom

    # Nice class to hold a wall rect
    class Wall(object):
        def __init__(self, pos, walls=None):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

        level = [
            "WWWWWWWWWWWWWWWWWWWW",
            "W                  W",
            "W         WWWWWW   W",
            "W   WWWW       W   W",
            "W   W        WWWW  W",
            "W WWW  WWWW        W",
            "W   W     W W      W",
            "W   W     W   WWW WW",
            "W   WWW WWW   W W  W",
            "W     W   W   W W  W",
            "WWW   W   WWWWW W  W",
            "W W      WW        W",
            "W W   WWWW   WWW   W",
            "W     W    E   W   W",
            "WWWWWWWWWWWWWWWWWWWW",
        ]

        # Parse the level string above. W = wall, E = exit
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
    # Initialise pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # Set up the display
    pygame.display.set_caption("Get to the red square!")
    screen = pygame.display.set_mode((320, 240))

    clock = pygame.time.Clock()
    walls = []  # List to hold the walls
    mario = Mario()  # Create the mario  # Move the mario if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            mario.move(-2, 0)
        if key[pygame.K_RIGHT]:
            mario.move(2, 0)
        if key[pygame.K_UP]:
            mario.move(0, -2)
        if key[pygame.K_DOWN]:
            mario.move(0, 2)

 #re-draw

	screen.fill(255, 255, 255)
	for row in range(col_count):
		for col in range(row_count):
			#row, col
			x = col * square_width - square_width /2 + 20
			y = row * square_height - square_height /2 + 20
			screen.blit(square_image, (x,y))

	mario_x = mario_col * square_width - square_width /2 + 20
	mario_y = mario_row * square_height - square_height /2 + 20

	box_x = box_col * square_width - square_width /2 + 20
	box_y = box_row * square_height - square_height /2 + 20

	#screen.blit(square_image, (20,20))
	screen.blit(mario_image, (mario_x, mario_y))
	screen.blit(box_image, (box_x, box_y))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
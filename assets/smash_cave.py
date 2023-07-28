import pygame
from menu1 import path
from smashers import MegaMan

pygame.init()
game_paused = False

# create a game window

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load background image

bg_image = pygame.image.load(path("selection|maps|cave.png")).convert_alpha()

# function for drawing background

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# game loop
player1 = MegaMan(75, 645, 1, [pygame.K_w, pygame.K_a, pygame.K_d], 4)
player2 = MegaMan(1125, 645, 1, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)

run = True
while run:

    # draw background

    draw_bg()
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    player1.draw(screen)
    player2.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    player2.draw(screen)
    # event handler

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display

    pygame.display.flip()
    
# exit pygame

pygame.quit()

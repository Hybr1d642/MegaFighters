import pygame
from menu1 import path

pygame.init()

# create a game window

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load background image

bg_image = pygame.image.load(path("selection|gui|map_select.png")).convert_alpha()

# load buttons

cave = pygame.image.load(path("selection|maps|cave.png")).convert_alpha()
forest = pygame.image.load(path("selection|maps|forest.png")).convert_alpha()
outside = pygame.image.load(path("selection|maps|outside.png")).convert_alpha()

# function for drawing background

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    
# button class

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def buttons(self):
        
        action = False

        # get mouse position

        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions

        if pygame.mouse.get_pressed()[0] and not self.clicked and self.rect.collidepoint(pos[0], pos[1]):
            self.clicked = True
            action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create buttons
cave_scaled = pygame.transform.scale(cave, (456, 236))
cave_pic = Button(90, 162, cave_scaled, 1)
forest_pic = Button(660, 162, forest, 1)
outside_pic = Button(370, 480, outside, 1)


def draw_map_selection():
    # draw background

    draw_bg()

    # draw buttons

    if cave_pic.buttons():
        import smash_cave

    if forest_pic.buttons():
        import smash_forest

    if outside_pic.buttons():
        import smash_outside
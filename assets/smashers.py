import pygame
from menu1 import path


class MegaMan:
    def __init__(self, x, y, player, controls, starting_direction):
        self.x = x
        self.y = y
        self.controls = controls
        self.standing_previous = False
        self.previous_direction = None
        self.moving = False
        self.jump_costume = 4
        self.jumping_check = False
        self.jump_index = 0
        self.jumping_animation_index = 0
        self.vel_y = 0
        self.player = player
        self.jumping = []
        self.jumping_2 = []
        self.running = []
        self.running_2 = []
        self.spawn = []
        self.spawn_2 = []
        self.stand = []
        self.stand_2 = []
        self.counter = 0
        self.direction = starting_direction
        self.index = 0
        for i in range(13):
            image = pygame.image.load(path(f"smashers|running_{i}.png")).convert_alpha()
            self.running.append(image)
            self.running_2.append(pygame.transform.flip(image, True, False))
        for i in range(15):
            image = pygame.image.load(path(f"smashers|spawn_{i}.png")).convert_alpha()
            self.spawn.append(image)
            self.spawn_2.append(pygame.transform.flip(image, True, False))
        for i in range(2):
            image = pygame.image.load(path(f"smashers|stand_{i}.png")).convert_alpha()
            self.stand.append(image)
            self.stand_2.append(pygame.transform.flip(image, True, False))
        for i in range(9):
            image = pygame.image.load(path(f"smashers|jump_{i}.png")).convert_alpha()
            self.jumping.append(image)
            self.jumping_2.append(pygame.transform.flip(image, True, False))
        if self.direction == 1:
            self.costume = self.stand_2[0]
        else:
            self.costume = self.stand[0]
        self.costume_rect = self.costume.get_rect()
        self.rect = pygame.Rect(x, y, self.costume_rect.width, self.costume_rect.height)

    def move(self, screen_width, screen_height):
        SPEED = 5
        GRAVITY = 0.1
        dx = 0
        dy = 0

        # Get keypresses

        key = pygame.key.get_pressed()

        # Movement
        if not self.jumping_check:
            self.moving = False
            if key[self.controls[1]]:
                self.standing_previous = False
                self.moving = True
                self.rect.x -= SPEED
                self.x -= SPEED
                if self.direction != 1:
                    self.direction = 1
                    self.costume = self.running_2[0]
                    self.index = 2
                    self.counter = 0
                elif self.direction == 1:
                    if self.counter == 10:
                        self.counter = 0
                        self.index += 1
                        if self.index == 10:
                            self.index = 2
                        print(self.index)
                        self.costume = self.running_2[self.index]
                    else:
                        self.counter += 1
                        self.costume = self.running_2[self.index]
            if key[self.controls[2]]:
                self.standing_previous = False
                self.moving = True
                self.rect.x += SPEED
                self.x += SPEED
                if self.direction != 4:
                    self.direction = 4
                    self.costume = self.running[0]
                    self.index = 2
                    self.counter = 0
                elif self.direction == 4:
                    if self.counter == 10:
                        self.counter = 0
                        self.index += 1
                        if self.index == 10:
                            self.index = 2
                        print(self.index)
                        self.costume = self.running[self.index]
                    else:
                        self.counter += 1
                        self.costume = self.running[self.index]
            if key[self.controls[0]]:
                self.moving = True
                self.jumping_check = True
            if not self.moving:
                if not self.standing_previous:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.costume = self.stand_2[self.index]
                    else:
                        self.costume = self.stand[self.index]
                    self.counter += 1
                else:
                    if self.counter == 50:
                        self.counter = 0
                        self.index += 1
                        if self.index > 1:
                            self.index = 0
                    self.counter += 1
                    print(self.direction)
                    if self.direction == 1:
                        self.costume = self.stand_2[self.index]
                    else:
                        self.costume = self.stand[self.index]
                    self.standing_previous = True

            # Jump

        elif self.jumping_check:
            self.jump_index += 1
            self.moving = True
            if self.direction == 1:
                if self.jump_index == 1:
                    self.costume = self.jumping_2[0]
                    print("costume 1")
                elif self.jump_index == 17:
                    self.costume = self.jumping_2[2]
                    print("costume7")
                elif 1 < self.jump_index < 17:
                    self.rect.y -= 17-self.jump_index
                    self.y -= 17 - self.jump_index
                    self.costume = self.jumping_2[1]
                    print("costume 2")
                    print("costume 3")
                elif 17 < self.jump_index < 33:
                    self.costume = self.jumping_2[2]
                    self.rect.y += 33 - self.jump_index
                    self.y += 33 - self.jump_index
                    print("costume 4")
                elif 38 > self.jump_index > 32:
                    self.jumping_animation_index += 1
                    if self.jumping_animation_index == 20:
                        self.jumping_animation_index = 0
                        self.jump_index += 1
                        print(f"New Jump Index: {self.jump_index}")
                        self.jump_costume += 1
                    self.costume = self.jumping_2[self.jump_costume]
                    if self.jump_index == 38 or self.jump_index == 37:
                        self.jumping_check = False
                        self.moving = False
                        self.costume = self.jumping_2[8]
                        self.jump_index = 0
                        self.jump_costume = 0
                        print("costume 6")
                    print(f"costume 5 | Jump Index: {self.jump_index}")
            elif self.direction == 4:
                if self.jump_index == 1:
                    self.costume = self.jumping[0]
                    print("costume 1")
                elif self.jump_index == 17:
                    self.costume = self.jumping[2]
                    print("costume7")
                elif 1 < self.jump_index < 17:
                    self.rect.y -= 17-self.jump_index
                    self.y -= 17 - self.jump_index
                    self.costume = self.jumping[1]
                    print("costume 2")
                    print("costume 3")
                elif 17 < self.jump_index < 33:
                    self.costume = self.jumping[2]
                    self.rect.y += 33 - self.jump_index
                    self.y += 33 - self.jump_index
                    print("costume 4")
                elif 38 > self.jump_index > 32:
                    self.jumping_animation_index += 1
                    if self.jumping_animation_index == 20:
                        self.jumping_animation_index = 0
                        self.jump_index += 1
                        print(f"New Jump Index: {self.jump_index}")
                        self.jump_costume += 1
                    self.costume = self.jumping[self.jump_costume]
                    if self.jump_index == 38 or self.jump_index == 37:
                        self.jumping_check = False
                        self.moving = False
                        self.costume = self.jumping[8]
                        self.jump_index = 0
                        self.jump_costume = 0
                        print("costume 6")
                    print(f"costume 5 | Jump Index: {self.jump_index}")


        # Ensure player stays on screen
        self.costume_rect = self.costume.get_rect()
        self.rect = pygame.Rect(self.x, self.y, self.costume_rect.width, self.costume_rect.height)

        if self.rect.x < 0:
            self.x = 0
        if self.rect.x + self.costume_rect.width > 1200 - self.costume_rect.width:
            print(self.rect.x + self.costume_rect.width)
            self.x = 1200 - self.costume_rect.width - 30
            print(self.x)
        if self.rect.y < 0:
            self.y = 0
        if self.rect.y + self.costume_rect.height > 800 - self.costume_rect.height:
            self.y = 800 - self.costume_rect.height

    def draw(self, surface: pygame.surface.Surface):
        scaled_costume = pygame.transform.scale(self.costume, (self.costume_rect.width * 2, self.costume_rect.height * 2))
        surface.blit(scaled_costume, (self.x, self.y))

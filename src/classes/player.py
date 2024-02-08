import pygame

import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, image):
        super().__init__()

        self.stand = pygame.Surface((w, h))
        self.stand.fill(image)
        self.super_jump_animation = []#[pygame.Surface((150, 200)), pygame.Surface((100, 180)), pygame.Surface((110, 150)), pygame.Surface((150, 100)), pygame.Surface((110, 150)), pygame.Surface((100, 180)), pygame.Surface((80, 210))]

        self.current_state = "stand"
        self.animation_index = 0

        self.image = self.stand
        self.rect = self.image.get_rect(topleft=(x, y))

        self.x = x
        self.y = y

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.dx = 0
        self.dy = 0
        self.walking_speed = 4
        self.jump_power = 8


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        #Anzeige für Objekt anpassen
        movement_enabled = kwargs.get("player_movement", False)
        for key, value in kwargs.items():

            if key == "stage":
                if value == "home":
                    #animationshandler
                    self._wackeln(y_factor)

                elif value == "walk_into_edeka":
                    #animationshandler
                    keys = pygame.key.get_pressed()
                    if self.y == int(Iheight*0.7):
                        if movement_enabled:
                            if keys[pygame.K_d] and not keys[pygame.K_a] and abs(self.dx) <= self.walking_speed:
                                self.dx += self.walking_speed*0.1
                            if keys[pygame.K_a] and not keys[pygame.K_d] and abs(self.dx) <= self.walking_speed:
                                self.dx -= self.walking_speed*0.1
                            if keys[pygame.K_SPACE]:
                                self.dy = -self.jump_power

                        if self.dx != 0: 
                            if abs(self.dx) <= 0.0000001:
                                self.dx = 0
                            else:   
                                self.dx -= self.dx/abs(self.dx)*0.1

                    self.dy += 0.5
                    if self.y + self.dy >= int(Iheight*0.7):
                        self.y = int(Iheight*0.7)
                        self.dy = 0
                    if -0.1 <= self.dx <= 0.1:
                        self.dx = 0

                    self.x += self.dx
                    self.y += self.dy

                    #handle animations
                    if self.dx == 0:
                        self._wackeln(y_factor)
                    else:
                        pass
                    #self.animation_index = int((self.animation_index + 0.1)) % len(self.get_current_animation())
                    #self.image = self.get_current_animation()[self.animation_index]
                
    def _wackeln(self, y_factor):
        #dynamische Bewegung des Spielers
        factor = (100 + 2*math.sin(pygame.time.get_ticks() * 0.005))/100

        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height() * factor))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y - (self.image.get_height() - self.height * y_factor)))

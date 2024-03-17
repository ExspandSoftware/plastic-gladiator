import pygame
import os

import math

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int):
        super().__init__()

        self.stand = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'player-stand-0.png'))
        self.stand = pygame.transform.scale(self.stand, (w, h))
        self.stand_l = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'player-stand-l.png'))
        self.stand_l = pygame.transform.scale(self.stand_l, (w, h))
        self.stand_r = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'player-stand-r.png'))
        self.stand_r = pygame.transform.scale(self.stand_r, (w, h))

        self.walk_right_1 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-r-1.png'))
        self.walk_right_1 = pygame.transform.scale(self.walk_right_1, (w+10, h))
        self.walk_right_2 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-r-2.png'))
        self.walk_right_2 = pygame.transform.scale(self.walk_right_2, (w+10, h))
        self.walk_right_3 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-r-3.png'))
        self.walk_right_3 = pygame.transform.scale(self.walk_right_3, (w+10, h))
        self.walk_right_4 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-r-4.png'))
        self.walk_right_4 = pygame.transform.scale(self.walk_right_4, (w+10, h))
        self.walk_right_5 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-r-5.png'))
        self.walk_right_5 = pygame.transform.scale(self.walk_right_5, (w+10, h))

        self.walk_left_1 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-l-1.png'))
        self.walk_left_1 = pygame.transform.scale(self.walk_left_1, (w+10, h))
        self.walk_left_2 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-l-2.png'))
        self.walk_left_2 = pygame.transform.scale(self.walk_left_2, (w+10, h))
        self.walk_left_3 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-l-3.png'))
        self.walk_left_3 = pygame.transform.scale(self.walk_left_3, (w+10, h))
        self.walk_left_4 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-l-4.png'))
        self.walk_left_4 = pygame.transform.scale(self.walk_left_4, (w+10, h))
        self.walk_left_5 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'player', 'walk-l-5.png'))
        self.walk_left_5 = pygame.transform.scale(self.walk_left_5, (w+10, h))

        self.last_direction = "right"

        self.walk_right = []
        self.walk_left = []

        self.current_state = "stand"
        self.animation_index = 0

        self.image = self.stand
        self.rect = self.image.get_rect(topleft=(x, y))

        self.step_sound = pygame.mixer.Sound("./assets/sounds/Step_Sound.mp3")
        self.step_stop = 0

        self.x = x
        self.y = y

        self.width = w
        self.height = h

        self.dx = 0
        self.dy = 0
        self.walking_speed = 5
        self.jump_power = 8


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        #Anzeige für Objekt anpassen
        movement_enabled = kwargs.get("player_movement", True)
        for key, value in kwargs.items():

            if key == "stage":
                if value == "home":
                    #animationshandler
                    #self._wackeln(y_factor)
                    pass

                elif value == "walk_into_edeka":
                    #animationshandler
                    keys = pygame.key.get_pressed()
                    if self.y == int(Iheight*0.675):
                        if movement_enabled:
                            if keys[pygame.K_d] and not keys[pygame.K_a] and abs(self.dx) <= self.walking_speed:
                                self.dx += self.walking_speed*0.1
                            if keys[pygame.K_a] and not keys[pygame.K_d] and abs(self.dx) <= self.walking_speed:
                                self.dx -= self.walking_speed*0.1
                            if keys[pygame.K_SPACE]:
                                self.dy = -self.jump_power

                        if self.dx != 0:
                            self.step_stop += 1
                            if self.step_stop >= 20:
                                pygame.mixer.Sound.play(self.step_sound)
                                self.step_stop = 0
                            if abs(self.dx) <= 0.1:
                                if self.dx < 0:
                                    self.last_direction = "left"
                                if self.dx > 0:
                                    self.last_direction = "right"
                                self.dx = 0
                            else:   
                                self.dx -= self.dx/abs(self.dx)*0.2*x_factor

                    self.dy += 0.5
                    if self.y + self.dy >= int(Iheight*0.675):
                        self.y = int(Iheight*0.675)
                        self.dy = 0

                    self.x += self.dx
                    self.y += self.dy

                elif value == "edeka":
                    #animationshandler
                    keys = pygame.key.get_pressed()
                    if self.y >= int(Iheight*0.4) - 1:
                        if movement_enabled:
                            if keys[pygame.K_d] and not keys[pygame.K_a] and abs(self.dx) <= self.walking_speed*1.25:
                                self.dx += self.walking_speed*0.125
                            if keys[pygame.K_a] and not keys[pygame.K_d] and abs(self.dx) <= self.walking_speed*1.25:
                                self.dx -= self.walking_speed*0.125
                            if keys[pygame.K_SPACE]:
                                self.dy = -self.jump_power*1.5

                        if self.dx != 0:
                            self.step_stop += 1
                            if self.step_stop >= 20:
                                pygame.mixer.Sound.play(self.step_sound)
                                self.step_stop = 0
                            if abs(self.dx) <= 0.1:
                                if self.dx < 0:
                                    self.last_direction = "left"
                                if self.dx > 0:
                                    self.last_direction = "right"
                                self.dx = 0
                            else:   
                                self.dx -= self.dx/abs(self.dx)*0.2*x_factor

                    self.dy += 0.75
                    if self.y + self.dy >= int(Iheight*0.4):
                        self.y = int(Iheight*0.4)
                        self.dy = 0

                    self.x += self.dx
                    self.y += self.dy
        
        self._animations()


    def _animations(self):
        if self.dx == 0:
            if self.last_direction == "left":
                self.image = self.stand_l
            else:
                self.image = self.stand_r
        
        elif self.dx > 0:
            match self.animation_index // 6:
                case 0:
                    self.image = self.walk_right_1
                case 1:
                    self.image = self.walk_right_2
                case 2:
                    self.image = self.walk_right_3
                case 3:
                    self.image = self.walk_right_4
                case 4:
                    self.image = self.walk_right_5

        elif self.dx < 0:
            match self.animation_index // 6:
                case 0:
                    self.image = self.walk_left_1
                case 1:
                    self.image = self.walk_left_2
                case 2:
                    self.image = self.walk_left_3
                case 3:
                    self.image = self.walk_left_4
                case 4:
                    self.image = self.walk_left_5

        self.animation_index = (self.animation_index + 1) % 30

    def _wackeln(self, y_factor):
        #dynamische Bewegung des Spielers
        factor = (100 + 2*math.sin(pygame.time.get_ticks() * 0.005))/100

        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height() * factor))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y - (self.image.get_height() - self.height*y_factor)))
    
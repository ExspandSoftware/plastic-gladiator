import pygame

from classes.player import Player

from config import *

class MinigamePlayer(Player):

    def __init__(self, x:int, y:int, width:int, height:int):
        super().__init__(x, y, width, height)

        self.image = self.stand
        self.walking_speed = 0.8
        self.update_count = 0

        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        """
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        

        #Anzeige für Objekt anpassen
        movement_enabled = kwargs.get("space_movement", True)
        for key, value in kwargs.items():

            keys = pygame.key.get_pressed()
            if movement_enabled:
                if keys[pygame.K_d] and not keys[pygame.K_a] and self.dx <= self.walking_speed:
                    self.dx += self.walking_speed*0.1
                if keys[pygame.K_a] and not keys[pygame.K_d] and -self.dx <= self.walking_speed:
                    self.dx -= self.walking_speed*0.1
                if not keys[pygame.K_d] and not keys[pygame.K_a] and self.dx != 0:
                    if abs(self.dx) <= 0.1:
                        if self.dx < 0:
                            self.last_direction = "left"
                        if self.dx > 0:
                            self.last_direction = "right"
                        self.dx = 0
                    else:
                        self.dx -= self.dx/abs(self.dx)*0.2#*x_factor

            if not (self.x + self.dx >= Iwidth*0.7 - 60 or self.x + self.dx <= Iwidth*0.3 + 10):
                self.x += self.dx
        
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

    def reset(self):
        self.x = Iwidth//2 - 25
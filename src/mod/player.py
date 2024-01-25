import pygame

import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, image):
        super().__init__()

        self.x = x
        self.y = y

        self.stand = pygame.Surface((w, h))
        self.stand.fill(image)
        self.super_jump_animation = []#[pygame.Surface((150, 200)), pygame.Surface((100, 180)), pygame.Surface((110, 150)), pygame.Surface((150, 100)), pygame.Surface((110, 150)), pygame.Surface((100, 180)), pygame.Surface((80, 210))]

        self.current_state = "stand"
        self.animation_index = 0

        self.image = self.stand
        self.rect = self.image.get_rect(topleft=(x, y))
        #Konstanten
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        for key, value in kwargs.items():

            if key == "stage":
                if value == "home":
                    #dynamische Bewegung dse Spielers
                    factor = (100 + 2*math.sin(pygame.time.get_ticks() * 0.005))/100

                    self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height() * factor))
                    self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y - (self.image.get_height() - self.height * y_factor)))

                elif value == "walk_into_edeka":
                    #andere Größe festlegen
                    factor = 0.5
                    self.x = Cwidth * 0.01
                    self.y = Cheight * 0.8
                    self.image = pygame.transform.scale(self.image, (self.width * factor, self.height * factor))
                    self.rect = self.image.get_rect(topleft=(self.x, self.y))



                    self.animation_index = int((self.animation_index + 0.1)) % len(self.get_current_animation())
                    self.image = self.get_current_animation()[self.animation_index]
                    

    def change_stage(self, new_stage):
        # Hier kannst du die Stage ändern und die Animationen entsprechend aktualisieren
        self.current_stage = new_stage
        self.animation_index = 0
        self.image = self.get_current_animation()[self.animation_index]
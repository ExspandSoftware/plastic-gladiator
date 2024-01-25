import pygame

import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int):
        super().__init__()

        self.stand = pygame.Surface((w, h))
        self.stand.fill((203, 178, 98))
        self.super_jump_animation = []#[pygame.Surface((150, 200)), pygame.Surface((100, 180)), pygame.Surface((110, 150)), pygame.Surface((150, 100)), pygame.Surface((110, 150)), pygame.Surface((100, 180)), pygame.Surface((80, 210))]

        self.current_state = "stand"
        self.animation_index = 0
        
        self.image = self.stand
        self.width = self.image.get_width() / 1280
        self.height = self.image.get_height() / 720
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x / 1280
        self.y = y / 720


    def update(self, *args, **kwargs):

        for key, value in kwargs.items():

            if key == "width":
                self.image = pygame.Surface((self.width * value, self.image.get_height()))
                self.image.fill((203, 178, 98))
                self.rect.centerx = self.x * value
            if key == "height":
                self.height = self.height * value / 720
                self.image = pygame.Surface((self.image.get_width(), self.height * value))
                self.image.fill((203, 178, 98))
                self.rect.centery = self.y * value
                self.y = self.y * value / 720

            if key == "stage":
                if value == "home":
                    #Player zentrieren

                    #dynamische Bewegung dse Spielers
                    factor = (100 + 2*math.sin(pygame.time.get_ticks() * 0.005))/100
                    new_height = int(self.height * 720*factor)

                    self.rect = self.image.get_rect(topleft=(self.rect.x, self.y - (new_height - self.height * 720)))
                    self.image = pygame.transform.scale(self.image, (self.image.get_width(), new_height))

                elif value == "level_1":
                    self.animation_index = int((self.animation_index + 0.1)) % len(self.get_current_animation())
                    self.image = self.get_current_animation()[self.animation_index]

        # Dynamische Anpassung der Größe an die Fenstergröße
        #screen_width, screen_height = pygame.display.get_surface().get_size()
        #new_width = int(screen_width/12)  # Beispielbreite
        #new_height = int(screen_height/4)  # Beispielhöhe

        #self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def change_stage(self, new_stage):
        # Hier kannst du die Stage ändern und die Animationen entsprechend aktualisieren
        self.current_stage = new_stage
        self.animation_index = 0
        self.image = self.get_current_animation()[self.animation_index]

    def get_current_animation(self):
        if self.current_state == "stand":
            return self.stand_animation
        elif self.current_state == "super_jump":
            return self.super_jump_animation
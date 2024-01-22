import pygame

import sys
sys.path.append('..')

from ..config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.stand_animation = [pygame.Surface((200, 400)), pygame.Surface((200, 405)), pygame.Surface((200, 410)), pygame.Surface((200, 405))]
        self.super_jump_animation = [pygame.Surface((150, 200)), pygame.Surface((100, 180)), pygame.Surface((110, 150)), pygame.Surface((150, 100)), pygame.Surface((110, 150)), pygame.Surface((100, 180)), pygame.Surface((80, 210))]

        self.current_state = "stand"
        self.animation_index = 0
        self.image = self.stand_animation[self.animation_index]
        self.rect = self.image.get_rect(topleft=(x, y))


    def update(self):
        self.animation_index = (self.animation_index + 1) % len(self.get_current_animation())
        self.image = self.get_current_animation()[self.animation_index]

        if STAGE == "home":
            pass

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
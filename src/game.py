#%% Imports ----------------------------------------------------------------
import pygame

import sys
import os

from .player import Player

#&& Class ------------------------------------------------------------------
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(400, 300)
        self.all_sprites.add(self.player)

        # Hier können weitere Initialisierungen vorgenommen werden

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()

            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

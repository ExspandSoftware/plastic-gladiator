import pygame
import os

from config import *

class PlasticBag(pygame.sprite.Sprite):

    def __init__(self, x:int, y:int, scale:int):
        super().__init__()

        self.scale = scale
        self.size = 30 * scale
        self.image = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', 'space', 'plastic_bag.png'))
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args, **kwargs):
        pass
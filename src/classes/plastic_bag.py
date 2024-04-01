import pygame
import os
import random

from config import *

class PlasticBag(pygame.sprite.Sprite):

    def __init__(self, x:int, y:int, scale:int):
        super().__init__()

        self.scale = scale
        self.size = 30 * scale
        image1 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', 'space', 'plastic_bag.png'))
        image2 = pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', 'space', 'waste-1.png'))
        self.image = random.choice([image1, image2])
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args, **kwargs):
        pass
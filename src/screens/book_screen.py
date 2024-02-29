import pygame

from config import *

class BookScreen(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, page_image, pages, current_page):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        
        # other vars
        self.current_page = current_page
        self.pages = pages

        self.background = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 150))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        # Scale objects
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
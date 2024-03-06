import pygame

from config import *

class DepositeMachine(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.interface = pygame.image.load(image)
        self.interface = pygame.transform.scale(self.interface, (self.interface.get_width() * 35, self.interface.get_height() * 35))

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2-self.interface.get_width()//2, -self.interface.get_height()*0.15)))

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
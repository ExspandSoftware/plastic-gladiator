import pygame

from config import *

class Inventory(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.number_of_items = 5
        self.interface = pygame.Surface((Iheight*0.2*self.number_of_items, Iheight*0.2))
        inventory_frame = pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "buttons", "inventory_frame.png"))
        inventory_frame = pygame.transform.scale(inventory_frame, (Iheight*0.2, Iheight*0.2))
        #draw the inventory frames
        for i in range(self.number_of_items):
            self.interface.blit(inventory_frame, (Iheight*0.2*i, 0))

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2 - self.interface.get_width()//2, Iheight//2 - self.interface.get_height()//2)))

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
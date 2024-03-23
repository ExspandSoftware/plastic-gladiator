import pygame

from functions.basic_rect import basic_rect

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
        self.items = [
            [pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Plastik-Flasche-mit-Pfand.png")), 5],
            [pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "edeka", "space", "bag.png")), 1],
            [pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "comp", "book.png")), 3],
            [pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "comp", "case.png")), 1],
        ]
        for item in self.items:
            item[0] = pygame.transform.scale(item[0], (Iheight*0.15, Iheight*0.15))
        self.number_of_items = len(self.items)
        self.interface = pygame.Surface((Iheight*0.2*self.number_of_items, Iheight*0.2))
        #self.inventory_frame = pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "buttons", "inventory_frame.png"))
        #self.inventory_frame = pygame.transform.scale(self.inventory_frame, (Iheight*0.2, Iheight*0.2))
        self.inventory_frame = basic_rect(Iheight*0.2, Iheight*0.2)
        #draw the inventory frames
        for i in range(self.number_of_items):
            self.interface.blit(self.inventory_frame, (Iheight*0.2*i, 0))

        self.font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 20)

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        
        #drawing the items into the inventory
        #draw the inventory frames
        for i in range(self.number_of_items):
            self.interface.blit(self.inventory_frame, (Iheight*0.2*i, 0))
            self.interface.blit(self.items[i][0], (Iheight*0.2*i + Iheight*0.1 - self.items[i][0].get_width()//2, Iheight*0.1 - self.items[i][0].get_height()//2))

            text = self.font.render(str(self.items[i][1])+"x", True, (255, 255, 255))
            self.interface.blit(text, (Iheight*0.2*i + Iheight*0.175 - text.get_width(), Iheight*0.18 - text.get_height()))


        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2 - self.interface.get_width()//2, Iheight//2 - self.interface.get_height()//2)))

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
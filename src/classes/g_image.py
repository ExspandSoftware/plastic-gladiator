import pygame

from functions.basic_rect import basic_rect

class GImage(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image, background:bool = True):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = basic_rect(width, height)
        if type(image) == str:
            self.ground = pygame.image.load(image)
            if background:
                self.ground = pygame.transform.scale(self.ground, (self.width-30, self.height-30))
                self.image.blit(self.ground, (15, 15))
            else:
                self.image = self.ground

        self.rect = self.image.get_rect(topleft=(x, y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *vars, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))


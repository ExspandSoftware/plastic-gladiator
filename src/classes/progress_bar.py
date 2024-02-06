import pygame

from config import *

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, background_image, testtube_image):
        super().__init__()

        self.composition = pygame.Surface((width, height))
        self.composition.fill(background_image)

        self.testtube = pygame.Surface((width, height))
        self.testtube.fill(testtube_image)
        self.composition.blit(self.testtube)

        self.image = self.composition
        self.rect = self.image.get_rect(topleft=(x, y))


    def update_progress_bar(self, progress):
        

        pygame.draw.rect(self.progress_surface, self.progress_color, (0, 0, progress_width, self.progress_rect.height))

    def update(self):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        #progress bar updaten
        self.update_progress_bar()
import pygame
from config import *

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, background_image):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        
        # other vars
        self.background = pygame.Surface((width, height))
        self.background.fill(background_image)
        self.backgroundimage = background_image

        self.testtubes = [pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'progress_bar', 'Reagenzglas-'+str(i)+'.png')) for i in range(6)]

        self.update_progress_bar(0.0)


    def update_progress_bar(self, progress):
        #determine idx
        idx = int(progress/0.1667)

        # draw testtube
        self.background.fill(self.backgroundimage)

        self.testtubes = [pygame.transform.scale(self.testtubes[i], (self.width*0.72, self.height*0.9)) for i in range(6)]
        self.background.blit(self.testtubes[idx], self.testtubes[idx].get_rect(topleft=(75, 18)))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #progress bar updaten
        for key, value in kwargs.items():
            if key == 'progress':
                self.update_progress_bar(value)

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        
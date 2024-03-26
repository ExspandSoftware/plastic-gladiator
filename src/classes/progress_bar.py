import pygame

from config import *
from functions.basic_rect import basic_rect

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.testtubes = [pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'home', 'progress_bar', 'Reagenzglas-'+str(i)+'.png')) for i in range(6)]
        self.testtubes = [pygame.transform.scale(self.testtubes[i], (self.width*0.72, self.height*0.9)) for i in range(6)]

        #update the bar for the first time
        self.update_progress_bar(0.0)


    def update_progress_bar(self, progress):
        #set the background for the element
        self.background = basic_rect(self.width, self.height)

        #determine idx
        idx = int(progress/0.2)%len(self.testtubes)

        # draw testtube
        self.background.blit(self.testtubes[idx], self.testtubes[idx].get_rect(topleft=(75, 18)))

        #draw Process Text
        font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 75)
        text = font.render('PROGRESS', True, (255, 255, 255))
        text = pygame.transform.rotate(text, 90)
        self.background.blit(text, (20, (self.height-text.get_height())//2))

        font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 50)
        text = font.render(f'{int(progress*100)}%', True, (255, 255, 255))
        text = pygame.transform.rotate(text, 90)
        self.background.blit(text, (76, (self.height-text.get_height())//2))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #progress bar updaten
        for key, value in kwargs.items():
            if key == 'progress':
                self.update_progress_bar(value)

        """
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
        """

        
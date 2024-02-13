import pygame

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, background_image, testtube_image):
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

        self.testtube = pygame.Surface((self.width*0.35, self.height*0.95))
        self.testtube.fill(testtube_image)

        self.update_progress_bar(0.0)


    def update_progress_bar(self, progress):
        # draw testtube
        self.background.fill(self.backgroundimage)
        self.background.blit(self.testtube, self.testtube.get_rect(topleft=(int(self.x+self.width*0.5), self.height*0.025)))

        # calculate the bar height and draw it
        bar_height = self.height*0.1 + progress*self.height*0.7
        pygame.draw.rect(self.background, (50, 175, 10), (int(self.x + self.width*0.525), self.height*0.9 - bar_height, self.width*0.3, bar_height))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        #progress bar updaten
        for key, value in kwargs.items():
            if key == 'progress':
                self.update_progress_bar(value)

        
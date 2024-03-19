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

        #work by intervals
        self.time_interval = pygame.time.get_ticks()
        self.interval_ms = 500
        img_1 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_1.fill((0, 200, 100))
        img_2 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_2.fill((0, 180, 80))
        img_3 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_3.fill((0, 160, 60))
        img_4 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_4.fill((0, 140, 40))
        img_5 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_5.fill((0, 120, 20))
        img_6 = pygame.Surface((600, 600), pygame.SRCALPHA)
        img_6.fill((0, 100, 0))
        self.it_idx = 0
        self.put_bottle = [
            img_1,
            img_2,
            img_3,
            img_4,
            img_5,
            img_6,
        ]
        self.it = 0

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        self.image.fill((0, 0, 0, 150))

        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2-self.interface.get_width()//2, -self.interface.get_height()*0.15)))

        #draw the insert bottle animation in a loop
        if self.it < 5:
            self.image.blit(self.put_bottle[self.it_idx], (Iwidth//2-self.put_bottle[self.it_idx].get_width()//2 - 150, Iheight-self.put_bottle[self.it_idx].get_height()))
            if pygame.time.get_ticks() - self.time_interval > self.interval_ms:
                self.time_interval = pygame.time.get_ticks()
                self.it_idx += 1
            if self.it_idx >= len(self.put_bottle):
                self.it_idx = 0
                self.it += 1
        else:
            #close the window automatically after the time has finished
            if "game_class" in kwargs:
                value = kwargs["game_class"]
                value.edeka_buttons_pressable = True
                value.movement = True
                value.active_sprites.remove(value.deposit_machine)
                value.active_sprites.remove(value.close_button)

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
import pygame
import random

from functions.basic_rect import basic_rect

from classes.minigame_player import MinigamePlayer
from classes.plastic_bag import PlasticBag

from config import *

class Space(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.interface = basic_rect(Iwidth*0.4, Iheight*0.9)
        # self.interface.fill((167, 234, 100))

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.plastic_bags = []
        self.max_bags = 20
        self.bags_left = self.max_bags
        self.time_before_next_bag = 0
        self.t1 = pygame.time.get_ticks()

        self.minigame_player = MinigamePlayer(Iwidth*0.3 + 10, Iheight*0.9 - 25, 50, 50)

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2 - self.interface.get_width()//2, Iheight//2 - self.interface.get_height()//2)))

        """
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self._run_game()
    
    def _run_game(self):
        if len(self.plastic_bags) != 0:
            for bag in self.plastic_bags:
                self.image.blit(bag.image, (bag.rect.x, bag.rect.y + 2))
                bag.rect = bag.image.get_rect(topleft=(bag.rect.x, bag.rect.y + 2))

                if bag.rect.y > Iheight * 0.9 - 30:
                    self.plastic_bags.remove(bag)

                if bag.rect.colliderect(self.minigame_player.rect):
                    self.plastic_bags.remove(bag)
                    self.bags_left += 1
        
        if len(self.plastic_bags) < self.max_bags and self.bags_left != 0 and pygame.time.get_ticks() - self.t1 > self.time_before_next_bag:
            self.time_before_next_bag = random.randint(300, 800)
            self.t1 = pygame.time.get_ticks()
            self.plastic_bags.append(PlasticBag(random.randint(Iwidth*0.3 + 25, Iwidth*0.7 - 50), Iheight*0.05 + 25))
            self.bags_left -= 1

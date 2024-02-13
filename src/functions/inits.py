from classes.player import Player
from classes.button import Button
from classes.g_image import GImage
from classes.progress_bar import ProgressBar
from classes.memory import MemoryGame

from config import *

def init_home(self):
    # objects in the stage
    self.home_background        = GImage(0, 0, Iwidth, Iheight, (15, 34, 65))
    self.titel_name             = GImage(Iwidth//2 - int(Iwidth*0.2), int(Iheight*0.02), int(Iwidth*0.4), int(Iheight*0.25), (123, 65, 235))
    self.player                 = Player(Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2, (208, 157, 95))
    self.progress_bar           = ProgressBar(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.15), int(Iheight*0.5), (70, 200, 110), (165, 213, 25))
    self.settings_button        = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (234, 76, 198))
    self.start_button           = Button(int(Iwidth*0.73), int(Iheight*0.73), int(Iwidth*0.25), int(Iheight*0.25), (234, 201, 65))
    self.book                   = Button(int(Iwidth*0.02), int(Iheight*0.98 - int(Iwidth*0.15)), int(Iwidth*0.15), int(Iwidth*0.15), (176, 23, 205))

    #add those bjects to the right sprites group
    self.home_sprites.add(self.home_background)
    self.home_sprites.add(self.player)
    self.home_sprites.add(self.titel_name)
    self.home_sprites.add(self.progress_bar)
    self.home_sprites.add(self.settings_button)
    self.home_sprites.add(self.start_button)
    self.home_sprites.add(self.book)


def init_pre_edeka(self):
    # objects in the stage
    self.edeka_background       = GImage(0, 0, Iwidth, Iheight, (15, 65, 34))
    self.player                 = Player(int(Iwidth*0.1), -100, Iwidth//15, Iheight//5, (208, 157, 95))
    self.door_L                 = GImage(int(Iwidth*0.65), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))
    self.door_R                 = GImage(int(Iwidth*0.75), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))

    #add those objects to the right sprites group
    self.walk_into_edeka.add(self.edeka_background)
    self.walk_into_edeka.add(self.door_L)
    self.walk_into_edeka.add(self.door_R)
    self.walk_into_edeka.add(self.player)


def init_edeka_1(self):
    # objects in the stage
    self.edeka_1_Background     = GImage(0, 0, Iwidth, Iheight, (123, 53, 12))
    self.player                 = Player(int(Iwidth*0.1), int(Iheight*0.5), Iwidth//7.5, Iheight//2.5, (208, 157, 95))

    # add those objects to the right sprites group
    self.edeka_1.add(self.edeka_1_Background)
    self.edeka_1.add(self.player)
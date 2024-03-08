import pygame

from config import *

from classes.player import Player
from classes.button import Button
from classes.g_image import GImage
from classes.progress_bar import ProgressBar

edeka_stage = 1

#load images from assets from home folder
def load_image_asset(subfolder, file):
    if subfolder is not None:
        return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', subfolder, file)
    else:
        return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', file)

def handle_edeka(self):
    global edeka_stage

    #handle each stage individually
    if edeka_stage == 1:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            if not self.black_transition[0]:
                wait_before_transition = 1100 #in Milliseconds 

                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition//2:
                    pygame.mixer.Sound.play(self.whoosh_sound)
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "walk_into_edeka")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
                    edeka_stage = 1
        
        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            #load next stage and remove the old sprites from the sprites group
            #obejcts in stage 2
            self.active_sprites.add(self.edeka_2_background)
            self.active_sprites.add(self.memory_button)
            #remove
            self.active_sprites.remove(self.edeka_1_background)
            self.active_sprites.remove(self.deposit_machine_button)
            self.active_sprites.remove(self.deposit_machine_image)
            !!!!!!!!
            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 2

    elif edeka_stage == 2:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:

            #add stage 1 sprites
            #remove stage 2 sprites
            self.active_sprites.remove(self.edeka_2_background)
            self.active_sprites.remove(self.memory_button)
            
            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x += Iwidth
            #go to the next stage
            edeka_stage = 1

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            # obejcts in stage 3
            self.edeka_3_background         = GImage(Iwidth*2, 0, Iwidth, Iheight, load_image_asset('backgrounds', 'Fleischtheke.png'))
            self.space_button               = Button(Iwidth*2 + Iwidth//2 - 50, Iheight//2 - 50, 100, 100, (192, 160, 236))
            #remove

            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 3

    elif edeka_stage == 3:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            #obejcts in stage 2
            self.edeka_2_background         = GImage(Iwidth, 0, Iwidth, Iheight, load_image_asset('backgrounds', 'Suessigkeitentheke.png'))
            self.memory_button              = Button(Iwidth + Iwidth//2 - 50, Iheight//2 - 50, 100, 100, (192, 160, 236))
            #remove
            self.active_sprites.remove(self.edeka_3_background)
            self.active_sprites.remove(self.space_button)
            
            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x += Iwidth
            #go to the next stage
            edeka_stage = 2

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            # obejcts in stage 4
            self.edeka_4_background         = GImage(Iwidth*3, 0, Iwidth, Iheight, (12, 253, 123))
            #remove

            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 4

    elif edeka_stage == 4:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            for idx, sprite in enumerate(self.active_sprites):
                if idx == len(self.active_sprites) - 2 or idx == len(self.active_sprites) - 3:
                    pass
                else:
                    sprite.x += Iwidth
            #go to the next stage
            edeka_stage = 3

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            if not self.black_transition[0]:
                wait_before_transition = 1100 #in Milliseconds 

                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition//2:
                    pygame.mixer.Sound.play(self.whoosh_sound)
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "home")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
                    edeka_stage = 1
        

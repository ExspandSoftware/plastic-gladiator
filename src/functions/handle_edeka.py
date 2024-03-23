import pygame

from config import *

from classes.player import Player
from classes.button import Button
from classes.g_image import GImage
from classes.progress_bar import ProgressBar

from functions.remove_sprites import remove_sprites
from functions.inits import *
from functions.speech_bubble import speech_bubble

timer = 0
check = True

#load images from assets from home folder
def load_image_asset(subfolder, file):
    if subfolder is not None:
        return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', subfolder, file)
    else:
        return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', file)

def handle_edeka(self):
    global timer
    global check
    
    #handle each stage individually
    if self.edeka_stage == 1:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            if not self.black_transition[0]:
                wait_before_transition = 500 #in Milliseconds 

                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition//2:
                    pygame.mixer.Sound.play(self.whoosh_sound)
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "walk_into_edeka")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
                    self.edeka_stage = 1
                    
                    self.EI_2 = 0
                    self.sp_b_it = 0
        
        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_2(self)
            add_general(self)
            
            #move the player to the other side
            self.player.x -= Iwidth

            #go to the next stage
            self.edeka_stage = 2

    elif self.edeka_stage == 2:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_1(self)
            add_general(self)

            #move the player to the other side
            self.player.x += Iwidth

            #go to the next stage
            self.edeka_stage = 1

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_3(self)
            add_general(self)

            #move the player to the other side
            self.player.x -= Iwidth

            #go to the next stage
            self.edeka_stage = 3
            timer = pygame.time.get_ticks()

    elif self.edeka_stage == 3:

        #stop the players movement so that the dialog can be played
        if pygame.time.get_ticks() - timer > 500 and check:
            check = False
            self.movement = False

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_2(self)
            add_general(self)

            #move the player to the other side
            self.player.x += Iwidth
            
            #go to the next stage
            self.edeka_stage = 2

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_4(self)
            add_general(self)

            #move the player to the other side
            self.player.x -= Iwidth

            #go to the next stage
            self.edeka_stage = 4

    elif self.edeka_stage == 4:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            #remove all sprites
            remove_sprites(self)
            #add needed sprites
            add_edeka_3(self)
            add_general(self)

            #move the player to the other side
            self.player.x += Iwidth

            #go to the next stage
            self.edeka_stage = 3

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

                    self.EI_2 = 0
                    self.sp_b_it = 0
                    self.progress += 0.2
import pygame

from config import *

edeka_stage = 1

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
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "home")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
        
        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            for sprite in self.edeka:
                sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 2

    elif edeka_stage == 2:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            for sprite in self.edeka:
                sprite.x += Iwidth
            #go to the next stage
            edeka_stage = 1

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            for sprite in self.edeka:
                sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 3

    elif edeka_stage == 3:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            for sprite in self.edeka:
                sprite.x += Iwidth
            #go to the next stage
            edeka_stage = 2

        #open the next stage
        if self.player.x >= Iwidth - self.player.width//2:
            for sprite in self.edeka:
                sprite.x -= Iwidth
            #go to the next stage
            edeka_stage = 4

    elif edeka_stage == 4:

        #go back to the previous stage
        if self.player.x <= -self.player.width//2:
            for sprite in self.edeka:
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
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "home")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
        

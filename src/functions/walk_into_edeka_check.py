import pygame

from config import *

def walk_into_edeka(self):
        wait_before_transition = 1100 #in Milliseconds 
        
        #come back to home
        if self.player.x <= -self.player.width:
            if not self.black_transition[0]:
                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition//2:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "home")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
        
        #Open the doors to go into edeka
        if int(Iwidth*0.6 - Iwidth//15) <= self.player.x <= int(Iwidth*0.8) + self.door_R.width:
            if self.door_L.x - 2 >= int(Iwidth*0.55):
                self.door_L.x -= 2
            if self.door_R.x + 2 <= int(Iwidth*0.85):
                self.door_R.x += 2
        else:
            if self.door_L.x + 2 <= int(Iwidth*0.65):
                self.door_L.x += 2
            if self.door_R.x - 2 >= int(Iwidth*0.75):
                self.door_R.x -= 2

        if self.door_L.x - 2 <= int(Iwidth*0.65) and int(Iwidth*0.65 - Iwidth//15 * 0.667) <= self.player.x <= int(Iwidth*0.85 - Iwidth//15 * 0.333):
            if not self.black_transition[0]:
                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "edeka_1")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [int(Iwidth*0.05), -100, Iwidth//15, Iheight//5]
        
        elif not self.player.x <= -self.player.width and not int(Iwidth*0.65 - Iwidth//15 * 0.667) <= self.player.x <= int(Iwidth*0.85 - Iwidth//15 * 0.333):
            self.tmp_ticker_start = 0
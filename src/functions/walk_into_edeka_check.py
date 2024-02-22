import pygame

from config import *

secret_stage = False

def walk_into_edeka(self):
        global secret_stage
        wait_before_transition = 1100 #in Milliseconds 
        
        #come back to home
        if not secret_stage:
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
                        self.black_transition = (True, "edeka")
                        self.buttons_not_pressable = True
            elif not self.player.x <= -self.player.width and not int(Iwidth*0.65 - Iwidth//15 * 0.667) <= self.player.x <= int(Iwidth*0.85 - Iwidth//15 * 0.333):
                self.tmp_ticker_start = 0

            # open secret stage
            if self.player.x >= Iwidth - self.player.width//2:
                #shift the object in the stage
                for sprite in self.walk_into_edeka:
                    sprite.x -= Iwidth

                # open secret stage
                    secret_stage = True

        elif secret_stage:
            if self.player.x <= -self.player.width//2:
                #shift the object in the stage
                for sprite in self.walk_into_edeka:
                    sprite.x += Iwidth

                # open secret stage
                    secret_stage = False
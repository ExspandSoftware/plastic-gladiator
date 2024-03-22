import pygame

from config import *

secret_stage = False

def walk_into_edeka(self):
    global secret_stage
    wait_before_transition = 2000 #in Milliseconds 
    
    #come back to home
    if not secret_stage:
        if self.player.x <= -self.player.width:
            if not self.black_transition[0]:
                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition//2:
                    pygame.mixer.Sound.play(self.whoosh_sound)
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "home")
                    self.buttons_not_pressable = True
                    self.transition_player_info = [Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2]
        
        #Open the doors to go into edeka
        if self.door_x <= self.player.x <= self.door_x + self.door_w*2:
            if self.door_L.x - 2 >= self.door_x - self.door_w*0.9:
                self.door_L.x -= 2
            if self.door_R.x + 2 <= self.door_x + self.door_w*1.9:
                self.door_R.x += 2
        else:
            if self.door_L.x + 2 <= self.door_x:
                self.door_L.x += 2
            if self.door_R.x - 2 >= self.door_x + self.door_w:
                self.door_R.x -= 2

        if self.door_x <= self.player.x <= self.door_x + self.door_w:
            if not self.black_transition[0]:
                if self.tmp_ticker_start == 0:
                    self.tmp_ticker_start = pygame.time.get_ticks()
                
                elif pygame.time.get_ticks() - self.tmp_ticker_start >= wait_before_transition:
                    pygame.mixer.Sound.play(self.whoosh_sound)
                    self.tmp_ticker_start = pygame.time.get_ticks()
                    self.black_transition = (True, "edeka")
                    self.buttons_not_pressable = True
        elif not self.player.x <= -self.player.width and not self.door_x <= self.player.x <= self.door_x + self.door_w:
            self.tmp_ticker_start = 0

        # open secret stage
        if self.player.x >= Iwidth - self.player.width//2:
            #shift the object in the stage
            for idx, sprite in enumerate(self.active_sprites):
                if idx == 6 or idx == 7:
                    pass
                else:
                    sprite.x -= Iwidth

            # open secret stage
                secret_stage = True

    elif secret_stage:
        
        # go back to previous stage
        if self.player.x <= -self.player.width//2:
            #shift the object in the stage
            for idx, sprite in enumerate(self.active_sprites):
                if idx == 7 or idx == 6:
                    pass
                else:
                    sprite.x += Iwidth

            # open secret stage
                secret_stage = False

        #stop the player from leaving the screen
        if self.player.x >= Iwidth - self.player.width:
            self.player.x = Iwidth - self.player.width

        
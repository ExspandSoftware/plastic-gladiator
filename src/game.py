#%% Imports ----------------------------------------------------------------
import pygame

import sys
import os
import json
import math

from functions.draw_performance_data import draw_p_data
from functions.save_state import save_state
from functions.walk_into_edeka_check import walk_into_edeka
from functions.inits import init_home, init_pre_edeka, init_edeka_1

from screens.settings_screen import SettingsScreen
from screens.book_screen import BookScreen

from config import *

#%% Class ------------------------------------------------------------------
class Game:
    screen: pygame.display
    progress: int | float
    
    font_size: int = FONT_SIZE
    
    black_transition: tuple[bool, str | None] = (False, None)
    transition_player_info: list[int] = [None, None, None, None]
    tmp_ticker_start: int = 0
    
    home_buttons_pressable: bool = True
    show_settings: bool = False
    show_book: bool = False
    
    is_fullscreen: bool = False
    show_data: bool = False
    
    def __init__(self) -> None:

        def _try_load_from_json(path:str, key:str, default: str | int | float | bool) -> str | int | float | bool:
            try:
                with open(path, "r") as json_file:
                    data = json.load(json_file)
                    val = data.get(key, default)
            
            except (json.JSONDecodeError, FileNotFoundError):
                val = default
            
            return val

        #Pygame Window -----------------------------------------------------------------------------------------------------
        global monitor_size
        monitor_size                = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen                 = pygame.display.set_mode((Iwidth, Iheight), pygame.RESIZABLE)
        pygame.display.set_caption('Plastic Gladiator')
        pygame.display.set_icon(pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'Mülleimer.png')))

        #Game Variables ----------------------------------------------------------------------------------------------------
        #variables that should be saved for the next opening
        self.progress               = _try_load_from_json(os.path.join(WORKING_DIR, 'JSONs', 'GameState.json'), 'progress', 0)

        #update screen with data
        self.font_size              = FONT_SIZE
        self.toggle_data            = False

        #transitions
        self.black_transition       = (False, None)
        self.tmp_ticker_start       = 0

        #pop-up screens
        self.home_buttons_pressable = True
        self.show_settings = False
        self.show_book = False
        
        #Pygame Logik ------------------------------------------------------------------------------------------------------
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, self.font_size)

        #Sprite Groups -----------------------------------------------------------------------------------------------------
        self.STAGE = stage
        
        self.home_sprites = pygame.sprite.Group()
        self.walk_into_edeka = pygame.sprite.Group()
        self.edeka_1 = pygame.sprite.Group()

        # init the home stage
        init_home(self)


    # events ---------------------------------------------------------------------------------------------------------------
    def handle_events(self):
        #handle pygame events
        for event in pygame.event.get():
            # Before quitting the game, save all important variables
            if event.type == pygame.QUIT:
                self.__quit()

            # Work on key events
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_F1]:
                    self.show_data = not self.show_data
                
                if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]) and keys[pygame.K_f]:
                    self.is_fullscreen = not self.is_fullscreen
                    
                    if self.is_fullscreen:
                        self.screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((1280, 720) if monitor_size[0] <= 1920 else (1920, 1080), pygame.RESIZABLE)
                        
                        # Workaround for https://github.com/pygame/pygame/issues/3107 from the comment https://github.com/pygame/pygame/issues/3107#issuecomment-1146788096 
                        self.screen = pygame.display.set_mode((1280, 720) if monitor_size[0] <= 1920 else (1920, 1080), pygame.RESIZABLE)

            # run code for mouse clicks (buttons)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.STAGE == "home":
                        if self.settings_button.is_clicked(event.pos, self.home_buttons_pressable):
                            self.home_buttons_pressable = False
                            self.show_settings = True

                        if self.start_button.is_clicked(event.pos, self.home_buttons_pressable):
                            self.tmp_ticker_start = pygame.time.get_ticks()
                            self.black_transition = (True, "walk_into_edeka")
                            self.home_buttons_pressable = False
                            self.transition_player_info = [int(Iwidth*0.05), -100, Iwidth//15, Iheight//5]

                        if self.book.is_clicked(event.pos, self.home_buttons_pressable):
                            self.home_buttons_pressable = False
                            self.home_sprites.add(self.book_screen)
                            self.home_sprites.add(self.next_page)
                            self.home_sprites.add(self.last_page)
                            self.home_sprites.add(self.close_book)
                            self.show_book = True
                        
                        if self.close_book.is_clicked(event.pos, self.show_book):
                            self.home_buttons_pressable = True
                            self.home_sprites.remove(self.book_screen)
                            self.home_sprites.remove(self.next_page)
                            self.home_sprites.remove(self.last_page)
                            self.home_sprites.remove(self.close_book)
                            self.show_book = False

        # handle stage changes for different stages
        if self.STAGE == "walk_into_edeka":
            walk_into_edeka(self)
               

    # event loop -----------------------------------------------------------------------------------------------------------
    def run(self):
        running = True

        while running:
            #handle events and setup screen than update it
            self.handle_events()
            self.screen.fill((255, 255, 255))

            #update the the width and height for scaling
            self.update_wh()
            
            #update and draw objects for each stage
            if self.STAGE == "home":
                self.home_sprites.update(Iwidth, Iheight, Cwidth, Cheight, stage=self.STAGE, progress=self.progress)
                self.home_sprites.draw(self.screen)
            elif self.STAGE == "walk_into_edeka":
                self.walk_into_edeka.update(Iwidth, Iheight, Cwidth, Cheight, stage=self.STAGE, player_movement=self.movement)
                self.walk_into_edeka.draw(self.screen)
            elif self.STAGE == "edeka_1":
                self.edeka_1.update(Iwidth, Iheight, Cwidth, Cheight, stage=self.STAGE)
                self.edeka_1.draw(self.screen)

            #handle pop-up menues
            if self.show_settings:
                pass
            elif self.show_book:
                pass

            #do everything ontop of the game then end the frame
            self.transition_black(pygame.time.get_ticks(), self.tmp_ticker_start, self.black_transition[1])
            draw_p_data(self, Cwidth, self.STAGE)
            pygame.display.flip()

            self.clock.tick(60)

            #do calculations
            self.progress += 0.005
            if self.progress > 1.0:
                self.progress = 0.0

        pygame.quit()


    #transitions ------------------------------------------------------------------------------------------------------------------------------
    def transition_black(self, ticker, start, stage, **kwargs) -> None:
        if self.black_transition[0]:
            self.movement = False
            duration_ms = 2000 # in milliseconds
            Opacity = min(((math.e/(duration_ms*100))+1)**(-((ticker-(start+duration_ms//2))**2)), 1.0)*255
    def __init_home(self):
        # objects in the stage
        self.home_background        = GImage(0, 0, Iwidth, Iheight, (15, 34, 65))
        self.titel_name             = GImage(Iwidth//2 - int(Iwidth*0.2), int(Iheight*0.02), int(Iwidth*0.4), int(Iheight*0.25), (123, 65, 235))
        self.player                 = Player(Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2, (208, 157, 95))
        self.progress_bar           = ProgressBar(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.15), int(Iheight*0.5), (70, 200, 110), (165, 213, 25))
        self.settings_button        = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (234, 76, 198))
        self.start_button           = Button(int(Iwidth*0.73), int(Iheight*0.73), int(Iwidth*0.25), int(Iheight*0.25), (234, 201, 65))
        self.book                   = Button(int(Iwidth*0.02), int(Iheight*0.98 - int(Iwidth*0.15)), int(Iwidth*0.15), int(Iwidth*0.15), (176, 23, 205))
        
        self.book_screen            = BookScreen(0, 0, 1280, 720, None)
        self.next_page              = Button(int(Iwidth*0.05), int(Iheight * 0.45), int(Iwidth * 0.1), int(Iheight * 0.1), (123, 45, 167))
        self.last_page              = Button(int(Iwidth*0.85), int(Iheight * 0.45), int(Iwidth * 0.1), int(Iheight * 0.1), (123, 45, 167))
        self.close_book             = Button(int(Iwidth*0.9), int(Iheight * 0.05), int(Iwidth * 0.07), int(Iheight * 0.1), (180, 85, 17))
        
        #add those objects to the right sprites group
        self.home_sprites.add(self.home_background)
        self.home_sprites.add(self.player)
        self.home_sprites.add(self.titel_name)
        self.home_sprites.add(self.progress_bar)
        self.home_sprites.add(self.settings_button)
        self.home_sprites.add(self.start_button)
        self.home_sprites.add(self.book)

    
    def __init_pre_edeka(self):
        # objects in the stage
        self.edeka_background       = GImage(0, 0, Iwidth, Iheight, (15, 65, 34))
        self.door_L                 = GImage(int(Iwidth*0.65), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))
        self.door_R                 = GImage(int(Iwidth*0.75), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))

        #add those objects to the right sprites group
        self.walk_into_edeka.add(self.edeka_background)
        self.walk_into_edeka.add(self.door_L)
        self.walk_into_edeka.add(self.door_R)
        self.walk_into_edeka.add(self.player)
    

    def __init_edeka_1(self):
        # objects in the stage
        self.edeka_1_Background     = GImage(0, 0, Iwidth, Iheight, (123, 53, 12))

        # add those objects to the right sprites group
        self.edeka_1.add(self.edeka_1_Background)
        self.edeka_1.add(self.player)
    

    def transition_black(self, ticker, start, stage, player_info) -> None:
        global STAGE
        self.movement = False
        duration_ms = 2000 # in milliseconds
        Opacity = min(((math.e/(duration_ms*100))+1)**(-((ticker-(start+duration_ms//2))**2)), 1.0)*255

            semi_black_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            semi_black_surface.fill((0, 0, 0, Opacity))
            self.screen.blit(semi_black_surface, (0, 0))

            if abs(ticker - start - duration_ms//2) <= 15:
                #change stage and load sprites
                self.STAGE = stage
                if stage == "walk_into_edeka":
                    init_pre_edeka(self)
                elif stage == "edeka_1":
                    init_edeka_1(self)

            if ticker - start >= duration_ms:
                self.tmp_ticker_start = 0
                self.black_transition = (False, None)
                self.home_buttons_pressable = True
                self.movement = True
        else:
            return


    def update_wh(self):
        global Cwidth, Cheight
        info = pygame.display.Info()
        Cwidth, Cheight = info.current_w, info.current_h

        font_size_factor = min(Cwidth/Iwidth, Cheight/Iheight)
        self.font_size = int(FONT_SIZE * font_size_factor)
        self.font = pygame.font.Font(None, self.font_size)
            
    
    def __quit(self):
        #save game and quit
        save_state(self)
        
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    print("Plastic-Gladiator game.py should not be run as a standalone script! Please run main.py instead.")
    exit(1)
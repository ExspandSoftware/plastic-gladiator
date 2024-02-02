#%% Imports ----------------------------------------------------------------
import pygame
import psutil

import sys
import os
import json
import math

from modules.player import Player
from modules.button import Button
from modules.g_image import GImage
from config import *

#%% Class ------------------------------------------------------------------
class Game:

    def __init__(self) -> None:

        def _try_load_from_json(path:str, key:str, default):
            try:
                with open(path, 'r') as json_file:
                    data = json.load(json_file)
                    return data.get(key, default)
            except (json.JSONDecodeError, FileNotFoundError):
                return default

        #Pygame Window
        global monitor_size
        monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.fullscreen = False
        self.screen = pygame.display.set_mode((Iwidth, Iheight), pygame.RESIZABLE)
        pygame.display.set_caption('Plastic Gladiator')
        pygame.display.set_icon(pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'Mülleimer.png')))
        
        #Pygame Logik
        self.clock = pygame.time.Clock()
        self.black_transition = (False, None)
        self.transition_player_info = [None, None, None, None]
        self.tmp_ticker_start = 0

        self.home_buttons_pressable = True
        self.show_settings = False
        self.show_book = False

        self.movement = True

        #Sprite Groups
        self.home_sprites = pygame.sprite.Group()
        self.walk_into_edeka = pygame.sprite.Group()
        self.edeka_1 = pygame.sprite.Group()

        #Objekte für die verschiedenen Bilder
        self.home_background = GImage(0, 0, Iwidth, Iheight, (15, 34, 65))
        self.player = Player(Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2, (208, 157, 95))
        self.titel_name = GImage(Iwidth//2 - int(Iwidth*0.2), int(Iheight*0.02), int(Iwidth*0.4), int(Iheight*0.25), (123, 65, 235))
        self.progress_bar = GImage(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.15), int(Iheight*0.5), (70, 200, 110))
        self.settings_button = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (234, 76, 198))
        self.start_button = Button(int(Iwidth*0.68), int(Iheight*0.78), int(Iwidth*0.3), int(Iheight*0.2), (234, 201, 65))
        self.book = Button(int(Iwidth*0.02), int(Iheight*0.98 - int(Iwidth*0.15)), int(Iwidth*0.15), int(Iwidth*0.15), (176, 23, 205))

        self.edeka_background = GImage(0, 0, Iwidth, Iheight, (15, 65, 34))
        self.door_L = GImage(int(Iwidth*0.65), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))
        self.door_R = GImage(int(Iwidth*0.75), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))

        #Zuweisung der Objekte
        self.home_sprites.add(self.home_background)
        self.home_sprites.add(self.player)
        self.home_sprites.add(self.titel_name)
        self.home_sprites.add(self.progress_bar)
        self.home_sprites.add(self.settings_button)
        self.home_sprites.add(self.start_button)
        self.home_sprites.add(self.book)

        self.walk_into_edeka.add(self.edeka_background)
        self.walk_into_edeka.add(self.door_L)
        self.walk_into_edeka.add(self.door_R)
        self.walk_into_edeka.add(self.player)

        self.edeka_1.add(self.player)

        #game variables
        self.progress = _try_load_from_json(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "progress", 0)

        #update screen with data
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)  # Schriftart und Größe
        self.toggle_data = False


    def update_wh(self):
        global Cwidth, Cheight
        info = pygame.display.Info()
        Cwidth, Cheight = info.current_w, info.current_h


    def draw_p_data(self):
        Zeilenabstand = int(self.font_size)

        if self.toggle_data:
            #author
            author_text = self.font.render(f"Author: {EXPORT_VARS[0]}", True, (255, 255, 255))
            self.screen.blit(author_text, (10, 10 + Zeilenabstand * 0))
            #version
            version_text = self.font.render(f"Version: {EXPORT_VARS[1]}", True, (255, 255, 255))
            self.screen.blit(version_text, (10, 10 + Zeilenabstand * 1))
            #chief information officer
            cio_text = self.font.render(f"Chief Information Officer: {EXPORT_VARS[2]}", True, (255, 255, 255))
            self.screen.blit(cio_text, (10, 10 + Zeilenabstand * 2))
            #moderators
            mod_text = self.font.render(f"Moderators: {EXPORT_VARS[3]}", True, (255, 255, 255))
            self.screen.blit(mod_text, (10, 10 + Zeilenabstand * 3))
            #head
            head_text = self.font.render(f"Head: {EXPORT_VARS[5]}", True, (255, 255, 255))
            self.screen.blit(head_text, (10, 10 + Zeilenabstand * 4))
            #supervisor
            sv_text = self.font.render(f"Supervisor: {EXPORT_VARS[6]}", True, (255, 255, 255))
            self.screen.blit(sv_text, (10, 10 + Zeilenabstand * 5))

            #fps
            fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
            self.screen.blit(fps_text, (10, 10 + Zeilenabstand * 7))
            #cpu performance
            cpu_percent = psutil.cpu_percent()
            cpu_text = self.font.render(f"CPU: {cpu_percent}%", True, (255, 255, 255))
            self.screen.blit(cpu_text, (10, 10 + Zeilenabstand * 8))

            #team
            names = EXPORT_VARS[4].split(", ")
            lines = []
            current_line = ''

            #separate words and build different lines
            for name in names:
                test_line = current_line + name + ', '
                text_width, text_height = self.font.size(test_line)
                
                if text_width <= Cwidth/3:
                    current_line = test_line
                else:
                    lines.append(current_line.rstrip())
                    current_line = name + ', '

            lines.append(current_line.rstrip())
            lines[0] = "Team: " + lines[0]

            #draw different lines to the surface
            y = 10
            for idx, line in enumerate(lines):
                line_team_text = self.font.render(line, True, (255, 255, 255))
                text_rect = line_team_text.get_rect(right=Cwidth-10, top=y)
                self.screen.blit(line_team_text, text_rect)
                y += Zeilenabstand
    

    def transition_black(self, ticker, start, stage, player_info) -> None:
        global STAGE
        self.movement = False
        d = 2000 # in milliseconds
        I = min(((math.e/(d*100))+1)**(-((ticker-(start+d//2))**2)), 1.0)*255

        semi_black_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        semi_black_surface.fill((0, 0, 0, I))
        self.screen.blit(semi_black_surface, (0, 0))

        if abs(ticker - start - d//2) <= 15:
            STAGE = stage
                            
            self.player.x = player_info[0]
            self.player.y = player_info[1]
            self.player.width = player_info[2]
            self.player.height = player_info[3]

        if ticker - start >= d:
            self.tmp_ticker_start = 0
            self.black_transition = (False, None)
            self.home_buttons_pressable = True
            self.transition_player_info = [None, None, None, None]
            self.movement = True


    def handle_events(self):
        global STAGE      

        for event in pygame.event.get():
            
            #before quiting the game, save all important variables
            if event.type == pygame.QUIT:
                #first save all the game state
                with open(os.path.join(WORKING_DIR, 'JSONs', 'GameState.json'), 'w') as f:
                    data = {
                        'progress': self.progress,
                    }
                    json.dump(data, f, indent=4)

                #then quit the game
                pygame.quit()
                sys.exit()

            #work on key events
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_F1]:
                    self.toggle_data = not self.toggle_data
                
                if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]) and keys[pygame.K_f]:
                    self.fullscreen = not self.fullscreen
                    
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((1280, 720) if monitor_size[0] <= 1920 else (1920, 1080), pygame.RESIZABLE)

            #run code for mouse clicks (buttons)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if STAGE == "home":
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
                            self.show_book = True

        #handle stage changes for diffrent stages
        if STAGE == "walk_into_edeka":

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


    def run(self):
        running = True
        while running:
            self.handle_events()
            self.screen.fill((255, 255, 255))

            #update the the width and height for scaling
            self.update_wh()
            
            #update and draw objects for each stage
            if STAGE == "home":
                self.home_sprites.update(Iwidth, Iheight, Cwidth, Cheight, stage=STAGE)
                self.home_sprites.draw(self.screen)
            elif STAGE == "walk_into_edeka":
                self.walk_into_edeka.update(Iwidth, Iheight, Cwidth, Cheight, stage=STAGE, player_movement=self.movement)
                self.walk_into_edeka.draw(self.screen)
            elif STAGE == "edeka_1":
                self.edeka_1.update(Iwidth, Iheight, Cwidth, Cheight, stage=STAGE)
                self.edeka_1.draw(self.screen)

            #handle transitions
            if self.black_transition[0]:
                self.transition_black(pygame.time.get_ticks(), self.tmp_ticker_start, self.black_transition[1], self.transition_player_info)

            #do everything ontop of the game then end the frame
            self.draw_p_data()
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

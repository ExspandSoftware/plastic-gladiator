#%% Imports ----------------------------------------------------------------
import pygame
import psutil

import sys
import os

from mod.player import Player
from mod.button import Button
from mod.g_image import GImage
from config import *

#%% Class ------------------------------------------------------------------
class Game:
    def __init__(self):
        #Pygame Window
        global monitor_size
        monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.fullscreen = False
        self.stage_change_wait = 0
        self.screen = pygame.display.set_mode((Iwidth, Iheight), pygame.RESIZABLE)
        pygame.display.set_caption('Plastic Gladiator')
        pygame.display.set_icon(pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'Mülleimer.png')))
        #Pygame Logik
        self.clock = pygame.time.Clock()

        #Sprite Groups
        self.home_sprites = pygame.sprite.Group()
        self.walk_into_edeka = pygame.sprite.Group()
        self.level_1_sprites = pygame.sprite.Group()
        self.level_2_sprites = pygame.sprite.Group()

        #Objekte für die verschiedenen Bilder
        self.home_background = GImage(0, 0, Iwidth, Iheight, (15, 34, 65))
        self.player = Player(Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight//2, (208, 157, 95))
        self.titel_name = GImage(Iwidth//2 - int(Iwidth*0.2), int(Iheight*0.02), int(Iwidth*0.4), int(Iheight*0.25), (123, 65, 235))
        self.progress_bar = GImage(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.15), int(Iheight*0.5), (70, 200, 110))
        self.settings_button = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (234, 76, 198))
        self.start_button = Button(int(Iwidth*0.68), int(Iheight*0.78), int(Iwidth*0.3), int(Iheight*0.2), (234, 201, 65))
        self.book = Button(int(Iwidth*0.02), int(Iheight*0.98 - int(Iwidth*0.15)), int(Iwidth*0.15), int(Iwidth*0.15), (176, 23, 205))

        self.edeka_background = GImage(0, 0, Iwidth, Iheight, (15, 65, 34))
        self.edeka_door = GImage(int(Iwidth//2 * 1.33 - Iwidth//6), int(int(Iheight*0.7) + int(Iheight//5) - int(Iheight//3.5)), int(Iwidth//6), int(Iheight//3.5), (80, 120, 40))
        self.inner_edeka_door = GImage(int(Iwidth//2 * 1.33 - Iwidth//6 + Iwidth//15), int(int(Iheight*0.7) + int(Iheight//5) - int(Iheight//3.5)), int(Iwidth//6 - 2 * Iwidth//15), int(Iheight//3.5), (110, 160, 60))
        self.outer_edeka_door = GImage(int(Iwidth//2 * 1.33 - Iwidth//6 - 0.75 * Iwidth//15), int(int(Iheight*0.7) + int(Iheight//5) - int(Iheight//3.5)), int(Iwidth//6 + 1.5 * Iwidth//15), int(Iheight//3.5), (50, 80, 20))

        #Zuweisung der Objekte
        self.home_sprites.add(self.home_background)
        self.home_sprites.add(self.player)
        self.home_sprites.add(self.titel_name)
        self.home_sprites.add(self.progress_bar)
        self.home_sprites.add(self.settings_button)
        self.home_sprites.add(self.start_button)
        self.home_sprites.add(self.book)

        self.walk_into_edeka.add(self.edeka_background)
        self.walk_into_edeka.add(self.outer_edeka_door)
        self.walk_into_edeka.add(self.edeka_door)
        self.walk_into_edeka.add(self.inner_edeka_door)
        self.walk_into_edeka.add(self.player)

        #game variables
        self.progress = 0

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
    

    def transition_black(self):
        pass


    def handle_events(self):
        global STAGE

        #change stage from outside to inside after a given time
        if self.stage_change_wait >= 50:
                self.stage_change_wait = 0
                STAGE = "edeka"


        if STAGE == "walk_into_edeka":
            if pygame.sprite.collide_rect(self.player, self.outer_edeka_door):
                #door should open
                pass
                

            if pygame.sprite.collide_rect(self.player, self.inner_edeka_door):
                self.stage_change_wait += 1
            else:
                self.stage_change_wait = 0
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if STAGE == "home":
                        if self.settings_button.is_clicked(event.pos):
                            print("settings button")

                        if self.start_button.is_clicked(event.pos):
                            STAGE = "walk_into_edeka"
                            
                            self.player.x = int(Iwidth*0.05)
                            self.player.y = int(Iheight*0.7)
                            self.player.width = Iwidth//15
                            self.player.height = Iheight//5

                        if self.book.is_clicked(event.pos):
                            print("Book Button")


    def run(self):
        running = True
        while running:
            self.handle_events()
            self.screen.fill((255, 255, 255))

            self.update_wh()
            
            if STAGE == "home":
                self.home_sprites.update(Iwidth, Iheight, Cwidth, Cheight, stage=STAGE)
                self.home_sprites.draw(self.screen)
            elif STAGE == "walk_into_edeka":
                self.walk_into_edeka.update(Iwidth, Iheight, Cwidth, Cheight, stage=STAGE)
                self.walk_into_edeka.draw(self.screen)

            self.draw_p_data()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

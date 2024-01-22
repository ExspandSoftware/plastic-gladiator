#%% Imports ----------------------------------------------------------------
import pygame
import psutil

import sys
import os

from mod.player import Player
from config import *

#%% Class ------------------------------------------------------------------
class Game:
    def __init__(self):
        #general
        self.screen = pygame.display.set_mode((Cwidth, Cheight), pygame.RESIZABLE)
        pygame.display.set_caption('Plastic Gladiator')
        pygame.display.set_icon(pygame.image.load(os.path.join(WORKING_DIR, 'assets', 'images', 'Mülleimer.png')))
        self.clock = pygame.time.Clock()

        self.home_sprites = pygame.sprite.Group()
        self.level_1_sprites = pygame.sprite.Group()
        self.level_2_sprites = pygame.sprite.Group()
        
        self.player = Player(Cwidth//2, Cheight * 0.4)
        self.home_sprites.add(self.player)

        #update screen with data
        self.font_size = 24
        self.font = pygame.font.Font(None, self.font_size)  # Schriftart und Größe
        self.toggle_data = True


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

            #seperate words and build diffrent lines
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

            #draw diffent lines to the surface
            y = 10
            for idx, line in enumerate(lines):
                line_team_text = self.font.render(line, True, (255, 255, 255))
                text_rect = line_team_text.get_rect(right=Cwidth-10, top=y)
                self.screen.blit(line_team_text, text_rect)
                y += Zeilenabstand


    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_F1]:
                        self.toggle_data = not self.toggle_data


    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update_wh()
            self.screen.fill((35, 23, 11))
            
            if STAGE == "home":
                self.home_sprites.update(STAGE)
                self.home_sprites.draw(self.screen)

            self.draw_p_data()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

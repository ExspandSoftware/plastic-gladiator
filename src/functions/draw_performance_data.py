import psutil
import pygame

from config import *

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
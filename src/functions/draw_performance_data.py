import psutil
import pygame

from config import *

def draw_p_data(self, screen_width):
        line_spacing = FONT_SIZE
        extra_spacing = 0

        if self.toggle_data:
            data_pairs = {
                "Author": EXPORT_VARS[0],
                "Version": EXPORT_VARS[1],
                "Chief Information Officer": EXPORT_VARS[2],
                "Moderators": EXPORT_VARS[3],
                "Head": EXPORT_VARS[5],
                "Supervisor": EXPORT_VARS[6],
                "Sound": EXPORT_VARS[7],
                "Concept": EXPORT_VARS[8],
                "Graphics": EXPORT_VARS[9],
                "Quality Assurance": EXPORT_VARS[10],
                "FPS": int(self.clock.get_fps()),
                "CPU": f"{psutil.cpu_percent()}%"
            }
            
            for idx, (key, value) in enumerate(data_pairs.items()):
                text = self.font.render(f"{key}: {value}", True, (255, 255, 255))
                self.screen.blit(text, (10, 10 + line_spacing * (idx + extra_spacing)))

                if idx == 9:
                     extra_spacing += 1

            #team ----------------------------------------------------------------------------------------------------------
            names = EXPORT_VARS[4].split(", ")
            lines = []
            current_line = ""

            #separate words and build different lines
            for name in names:
                test_line = current_line + name + ", "
                text_width, text_height = self.font.size(test_line)
                
                if text_width <= Cwidth/3:
                    current_line = test_line
                else:
                    lines.append(current_line.rstrip())
                    current_line = name + ", "

            lines.append(current_line.rstrip())
            lines[0] = "Team: " + lines[0]

            #draw different lines to the surface
            y = 10
            for idx, line in enumerate(lines):
                line_team_text = self.font.render(line, True, (255, 255, 255))
                text_rect = line_team_text.get_rect(right=screen_width-10, top=y)
                self.screen.blit(line_team_text, text_rect)
                y += line_spacing
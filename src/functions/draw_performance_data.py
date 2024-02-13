import psutil

from config import EXPORT_VARS

def draw_p_data(self, screen_width: int, stage):
        line_spacing = self.font.size("TEST")[1] * 1.25
        extra_spacing = 0

        if self.show_data:
            left_text = {
                "Author": EXPORT_VARS[0],
                "Version": EXPORT_VARS[1],
                "Chief Information Officer": EXPORT_VARS[2],
                "Moderators": EXPORT_VARS[3],
                "Head": EXPORT_VARS[5],
                "Supervisor": EXPORT_VARS[6],
                "Sound": EXPORT_VARS[7],
                "Concept": EXPORT_VARS[8],
                "Graphics": EXPORT_VARS[9],
                "Chief Annoyance Officer": EXPORT_VARS[10],
                "FPS": int(self.clock.get_fps()),
                "CPU Usage": f"{psutil.cpu_percent()}%",
                "CPU Cores": f"{psutil.cpu_count(logical=False)}",
                "CPU logical Threads": f"{psutil.cpu_count(logical=True)}",
            }
            
            for idx, (key, value) in enumerate(left_text.items()):
                if key == "CPU Usage" or key == "FPS":
                     extra_spacing += 1
                
                text = self.font.render(f"{key}: {value}", True, (255, 255, 255))
                self.screen.blit(text, (10, 10 + line_spacing * (idx + extra_spacing)))


            # team ----------------------------------------------------------------------------------------------------------
            names = EXPORT_VARS[4].split(", ")
            right_text = []
            current_line = ""

            # separate words and build different lines
            for name in names:
                test_line = current_line + name + ", "
                text_width, text_height = self.font.size(test_line)
                
                if text_width <= screen_width/3:
                    current_line = test_line
                else:
                    right_text.append(current_line.rstrip())
                    current_line = name + ", "

            right_text.append(current_line.rstrip())
            right_text[0] = "Team: " + right_text[0]

            #add additional information
            right_text.append("Stage: " + f"\"{stage}\"")

            # draw different lines to the surface
            y = 10
            for idx, line in enumerate(right_text):
                line_text = self.font.render(line, True, (255, 255, 255))
                text_rect = line_text.get_rect(right=screen_width-10, top=y)
                self.screen.blit(line_text, text_rect)

                if idx == len(right_text)-2:
                    y += line_spacing
                y += line_spacing


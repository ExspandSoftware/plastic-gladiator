import pygame

from config import *
from functions.speech_bubble import speech_bubble

def handle_draws(self):
    if self.STAGE == "home":
        pass

    elif self.STAGE == "walk_into_edeka":
        pass

    elif self.STAGE == "edeka":

        if self.edeka_stage == 1:
            pass

        elif self.edeka_stage == 2:
            pass

        elif self.edeka_stage == 3:
            
            if self.sp_b_it == 1:
                text = "Moin! Ich nehme gerne ein Schnitzel im Broetchen mit Gewuerzketchup."
                sb = speech_bubble(text, 600, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 2:
                text = "Jo, gerne doch! Soll ich es noch einmal warm machen?"
                sb = speech_bubble(text, 700, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))
            
            elif self.sp_b_it == 3:
                text = "Ja gerne! Koennten Sie es mir dann auch direkt in meinen Beutel geben? Ich möchte gerne ein wenig auf Plastik im Alltag verzichten."
                sb = speech_bubble(text, 700, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 4:
                text = "Oh, das tut mir Leid... Das geht leider nicht. Firmen- und EU-Richtlinien..."
                sb = speech_bubble(text, 700, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))
            
            elif self.sp_b_it == 5:
                text = "Sind Sie sicher? Wie wäre es mit einer Wette? Wenn ich es schaffe allen Verpackungen auszuweichen, kriege ich das Broetchen so mit?"
                sb = speech_bubble(text, 700, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 6:
                text = "Nagut, mach dich bereit!"
                sb = speech_bubble(text, 700, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))

            elif self.sp_b_it == 7:
                self.edeka_buttons_pressable = False
                self.movement = False

                self.active_sprites.add(self.space)
                self.active_sprites.add(self.close_button)
            
            if pygame.time.get_ticks() - self.time_interval > self.interval_ms and self.sp_b_it <= 7:
                self.time_interval = pygame.time.get_ticks()
                self.sp_b_it += 1

        elif self.edeka_stage == 4:
            pass
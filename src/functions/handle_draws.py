import pygame
import random

from config import *
from functions.speech_bubble import speech_bubble

price = random.randint(3, 13)
cent = random.randint(97, 99)
price = str(price) + "," + str(cent)

def handle_draws(self, Cwidth, Cheight):
    global price

    if self.STAGE == "home":
        pass

    elif self.STAGE == "walk_into_edeka":
        pass

    elif self.STAGE == "edeka":

        if self.edeka_stage == 1:
            pass

        elif self.edeka_stage == 2:
            if self.EI_2 == 0:
                self.EI_2 = pygame.time.get_ticks()

            if pygame.time.get_ticks() - self.EI_2 <= 10000:
                text = "Nun mach deinen ersten Einkauf! Such dir etwas aus dem Regel aus - aber Achtung! Nimm lieber nicht das Falsche. Klick einfach auf das Regal und es beginnt..."
                sb = speech_bubble(text, Cwidth*0.9)
                self.screen.blit(sb, (Cwidth//2 - sb.get_width()//2, Cheight - 25 - sb.get_height()))

        elif self.edeka_stage == 3:
            
            if self.sp_b_it == 1:
                text = "Moin! Ich nehme gerne ein Schnitzel im Brötchen mit Gewürzketchup."
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 2:
                text = "Jo, gerne doch! Soll ich es noch einmal warm machen?"
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))
            
            elif self.sp_b_it == 3:
                text = "Ja gerne! Könnten Sie es mir dann auch direkt in meinen Beutel geben? Ich möchte gerne ein wenig auf Plastik im Alltag verzichten."
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 4:
                text = "Oh, das tut mir Leid... Das geht leider nicht. Firmen- und EU-Richtlinien..."
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))
            
            elif self.sp_b_it == 5:
                text = "Sind Sie sicher? Wie wäre es mit einer Wette? Wenn ich es schaffe allen Verpackungen auszuweichen, kriege ich das Brötchen so mit?"
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sp_b_it == 6:
                text = "Nagut, mach dich bereit!"
                sb = speech_bubble(text, (950-(self.player.x+self.player.width))*0.9, True, "r", 24)
                self.screen.blit(sb, (990 - sb.get_width(), 220 - sb.get_height()))

            elif self.sp_b_it == 7:
                self.edeka_buttons_pressable = False
                self.movement = False

                self.active_sprites.add(self.space)
                self.active_sprites.add(self.space.minigame_player)
                self.active_sprites.add(self.close_button)
            
            if not DEV_MODE:
                if pygame.time.get_ticks() - self.time_interval > self.interval_ms and self.sp_b_it <= 7:
                    self.time_interval = pygame.time.get_ticks()
                    self.sp_b_it += 1

            else:
                if pygame.time.get_ticks() - self.time_interval > 500 and self.sp_b_it <= 7:
                    self.time_interval = pygame.time.get_ticks()
                    self.sp_b_it += 1

        elif self.edeka_stage == 4:

            if self.sb_it == 1:
                text = f"Moin! Das macht einmal {price}€ bitte."
                sb = speech_bubble(text, 550, True, "r", 24)
                self.screen.blit(sb, (794 - sb.get_width(), 155 - sb.get_height()))
            
            elif self.sb_it == 2:
                text = "Hallo! Hier bitte. Und, wie hab ich mich geschlagen?"
                sb = speech_bubble(text, (794-(self.player.x+self.player.width))*0.9, True, "l", 24)
                self.screen.blit(sb, (self.player.x + self.player.width*0.7, self.player.y - sb.get_height() + 25))
            
            elif self.sb_it == 3:
                text = f"Sehr gut! Aber denk immer dran: Guck lieber zweimal hin, bevor du etwas kaufst. "
                sb = speech_bubble(text, 550, True, "r", 24)
                self.screen.blit(sb, (794 - sb.get_width(), 155 - sb.get_height()))

            elif self.sb_it == 4:
                text = f"Und halte den Abfall, den du produzierst immer möglichst gering. Es gibt viele Wege und Möglichkeiten sparsam zu sein..."
                sb = speech_bubble(text, 550, True, "r", 24)
                self.screen.blit(sb, (794 - sb.get_width(), 155 - sb.get_height()))
            
            elif self.sb_it == 5:
                self.edeka_buttons_pressable = True
                self.movement = True
            
            if not DEV_MODE:
                if pygame.time.get_ticks() - self.time_interval > self.interval_ms and self.sb_it <= 5:
                    self.time_interval = pygame.time.get_ticks()
                    self.sb_it += 1
            
            else:
                if pygame.time.get_ticks() - self.time_interval > 500 and self.sb_it <= 5:
                    self.time_interval = pygame.time.get_ticks()
                    self.sb_it += 1
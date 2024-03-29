import pygame
import json

from config import *

from classes.button import Button

from functions.basic_rect import basic_rect
from functions.save_state import save_state
from functions.remove_sprites import remove_sprites
import functions.inits as inits


class SettingsScreen(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.interface = basic_rect(Iwidth*0.8, Iheight*0.8)

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.padding = 100

        self.click_sound = pygame.mixer.Sound("./assets/sounds/button_click.mp3")

        #variables for the settings
        self.font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 50)
        self.volume = self._try_load_from_json(os.path.join(WORKING_DIR, 'JSONs', 'settings.json'), 'volume', 0.25)
        self.font_size = self._try_load_from_json(os.path.join(WORKING_DIR, 'JSONs', 'settings.json'), 'font_size', 50)


    def _try_load_from_json(self, path:str, key:str, default: str | int | float | bool) -> str | int | float | bool:
            try:
                with open(path, "r") as json_file:
                    data = json.load(json_file)
                    val = data.get(key, default)
            
            except (json.JSONDecodeError, FileNotFoundError):
                val = default
            
            return val


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.ix = Iwidth//2 - self.interface.get_width()//2
        self.iy = Iheight//2 - self.interface.get_height()//2
        self.image.blit(self.interface, self.interface.get_rect(topleft=(self.ix, self.iy)))

        # Zeige die Einstellungsoptionen an
        self.show_option("Lautstaerke:", str(self.volume*100)+"%", self.padding)
        self.show_option("Schriftgroesse:", self.font_size, self.padding + 50)

        # Zeige die Optionen zum Beenden/Speichern und zur Rückkehr zum Hauptmenü an
        #handle pygame events
        pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
                        
        self.show_button("Speichern", self.interface.get_height() - self.padding - 200, pos, clicked, self.save_settings, kwargs["game_class"])
        self.show_button("Zum Hauptmenue", self.interface.get_height() - self.padding - 100, pos, clicked, self.return_to_menu, kwargs["game_class"])

        """
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def show_option(self, text, value, y):
        text_surface = self.font.render(f"{text}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(self.padding, y))
        self.interface.blit(text_surface, text_rect)

        text_surface = self.font.render(f"{value}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(self.interface.get_width() - text_surface.get_width() - self.padding, y))
        self.interface.blit(text_surface, text_rect)

    
    def show_button(self, text, y, pos, clicked, action, game_obj):
        text_surface = self.font.render(f"{text}", True, (255, 255, 255))
        background = basic_rect(text_surface.get_width() + 50, text_surface.get_height() + 50)
        background.blit(text_surface, (25, 27))

        x = self.interface.get_width()//2 - background.get_width()//2
        self.interface.blit(background, (x, y))

        if (x <= pos[0] - self.ix <= x + background.get_width()) and (y <= pos[1] - self.iy <= y + background.get_height()) and clicked:
            action(game_obj)
            pygame.mixer.Sound.play(self.click_sound)


    def save_settings(self, game_obj):
        save_state(game_obj.progress, game_obj.secret_progress, self.font_size, self.volume)


    def return_to_menu(self, game_obj):
        print("aa")
        if not game_obj.black_transition[0]:
            print("bb")
            pygame.mixer.Sound.play(game_obj.whoosh_sound)
            game_obj.tmp_ticker_start = pygame.time.get_ticks()
            game_obj.black_transition = (True, "home")
            game_obj.transition_player_info = [533, 240, 213, 360]

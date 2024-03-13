import pygame

from config import *
from functions.basic_rect import basic_rect

class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value):
        self.rect = pygame.Rect(x, y, width, height)
        self.slider_rect = pygame.Rect(x, y, 10, height)
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value

    def update(self):
        # Aktualisiere die Position des Schiebereglers basierend auf dem Wert
        value_range = self.max_value - self.min_value
        normalized_value = (self.value - self.min_value) / value_range
        self.slider_rect.x = self.rect.x + int(normalized_value * (self.rect.width - self.slider_rect.width))

    def draw(self, screen):
        # Zeichne den Hintergrund und den Schieberegler
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.slider_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.slider_rect.collidepoint(event.pos):
                self.dragging = True

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # Aktualisiere den Wert basierend auf der horizontalen Mausbewegung
            mouse_x, _ = event.pos
            mouse_x = max(self.rect.x, min(self.rect.x + self.rect.width - self.slider_rect.width, mouse_x))
            value_range = self.max_value - self.min_value
            normalized_value = (mouse_x - self.rect.x) / (self.rect.width - self.slider_rect.width)
            self.value = int(normalized_value * value_range) + self.min_value

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False


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

        #variables for the settings
        self.font = pygame.font.Font(None, 50)
        self.volume = 50
        self.font_size = 24
        self.slider = Slider(500, 200, 300, 20, 0, 100, 50)

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.ix = Iwidth//2 - self.interface.get_width()//2
        self.iy = Iheight//2 - self.interface.get_height()//2
        self.image.blit(self.interface, self.interface.get_rect(topleft=(self.ix, self.iy)))

        # Zeige die Einstellungsoptionen an
        self.show_option("Lautstärke:", self.volume, 50)
        self.show_option("Schriftgröße:", self.font_size, 100)

        # Hier könntest du weitere Einstellungsoptionen hinzufügen

        # Zeige die Optionen zum Beenden/Speichern und zur Rückkehr zum Hauptmenü an
        self.show_option("Speichern", None, 200, action=self.save_settings)
        self.show_option("Zum Hauptmenü", None, 250, action=self.return_to_menu)

        #sliders
        for event in pygame.event.get():
            # Übergebe das Event an den Schieberegler
            self.slider.handle_event(event)
        self.slider.update()

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

    def draw(self, screen):
        self.slider.draw(screen)

    def show_option(self, text, value, y, action=None):
        text_surface = self.font.render(f"{text} {value}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(self.ix + 15, y))
        self.interface.blit(text_surface, text_rect)

        # Zeige den Cursor an, wenn die Option ausgewählt ist
        if action:
            pygame.draw.rect(self.interface, (255, 255, 255), text_rect, 2)
            mouse_pos = pygame.mouse.get_pos()
            if text_rect.collidepoint(mouse_pos):
                pygame.draw.line(self.interface, (255, 255, 255), (text_rect.left, text_rect.centery),
                                (text_rect.right, text_rect.centery), 2)

                # Führe die Aktion aus, wenn die linke Maustaste gedrückt wird
                if pygame.mouse.get_pressed()[0]:
                    action()

    def save_settings(self):
        print("Einstellungen gespeichert")

    def return_to_menu(self):
        print("Zum Hauptmenü zurückkehren")
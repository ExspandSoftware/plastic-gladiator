import pygame
import sys

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, progress_color, background_color, font, text_color):
        super().__init__()

        self.progress_color = progress_color
        self.background_color = background_color
        self.font = font
        self.text_color = text_color

        # Fortschrittsvariable (Wert zwischen 0 und 1)
        self.progress = 0.0

        # Erstelle eine Surface als Grundlage für die Fortschrittsleiste
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(topleft=(x, y))

        # Erstelle Rechtecke für Hintergrund- und Fortschrittsleiste
        self.background_rect = pygame.Rect(0, 0, width, height)
        self.progress_rect = pygame.Rect(0, 0, width, height)

    def update(self):
        # Berechne die Breite der Fortschrittsleiste basierend auf dem Fortschritt
        progress_width = int(self.progress * self.progress_rect.width)
        self.progress_rect.width = progress_width

        # Zeichne die Hintergrund- und Fortschrittsleiste
        self.surface.fill(self.background_color)
        pygame.draw.rect(self.surface, self.progress_color, self.progress_rect)

        # Zeichne den Fortschritts-Text
        progress_text = f"{int(self.progress * 100)}%"
        text_surface = self.font.render(progress_text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def set_progress(self, progress):
        # Stelle sicher, dass der Fortschritt zwischen 0 und 1 liegt
        self.progress = max(0.0, min(progress, 1.0))


# Initialisiere das Pygame-Fenster
screen_size = (400, 200)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Progress Bar Example")

# Erstelle eine Font für den Text
font = pygame.font.Font(None, 24)

# Erstelle eine Fortschrittsleiste
progress_bar = ProgressBar(50, 50, 300, 30, (0, 255, 0), (150, 150, 150), font, (255, 255, 255))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hier kannst du die Fortschrittsvariable aktualisieren
    # (angenommen, progress_variable ist der Fortschrittswert zwischen 0 und 1)
    progress_variable = 0.6
    progress_bar.set_progress(progress_variable)

    # Hier kannst du die Fortschrittsleiste aktualisieren und auf den Bildschirm zeichnen
    progress_bar.update()
    progress_bar.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

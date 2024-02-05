import pygame
import sys

pygame.init()

# Initialisiere das Pygame-Fenster
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Hauptfenster")

# Initialisiere das Einstellungsfenster
settings_screen_size = (400, 300)
settings_screen = pygame.Surface(settings_screen_size)
settings_screen.fill((200, 200, 200))  # Hintergrundfarbe des Einstellungsfensters

# Schaltflächen für Einstellungen
button_width, button_height = 100, 40
button_x, button_y = (settings_screen_size[0] - button_width) // 2, 50

button_font = pygame.font.Font(None, 36)
button_text_color = (0, 0, 0)
button_hover_color = (100, 100, 100)
button_normal_color = (150, 150, 150)

buttons = [
    {"text": "Option 1", "rect": pygame.Rect(button_x, button_y, button_width, button_height)},
    {"text": "Option 2", "rect": pygame.Rect(button_x, button_y + 60, button_width, button_height)},
]

def draw_buttons():
    for button in buttons:
        pygame.draw.rect(settings_screen, button_normal_color, button["rect"])
        pygame.draw.rect(settings_screen, button_text_color, button["rect"], 2)

        text_surface = button_font.render(button["text"], True, button_text_color)
        text_rect = text_surface.get_rect(center=button["rect"].center)
        settings_screen.blit(text_surface, text_rect)

def handle_button_click(mouse_pos):
    for button in buttons:
        if button["rect"].collidepoint(mouse_pos):
            print(f"Button '{button['text']}' wurde geklickt!")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                handle_button_click(mouse_pos)

    # Zeichne den Inhalt des Einstellungsfensters auf den Hauptbildschirm
    screen.blit(settings_screen, ((screen_size[0] - settings_screen_size[0]) // 2, (screen_size[1] - settings_screen_size[1]) // 2))

    draw_buttons()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

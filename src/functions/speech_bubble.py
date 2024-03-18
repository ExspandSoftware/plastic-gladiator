import pygame

from config import *

def speech_bubble(text, max_width):

    # modify the text --------------------------------------------------------------
    font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 48)
    words = text.split(' ')
    rendered_lines = []
    rendered_text = ''
    current_line = ''

    for word in words:
        # Füge das aktuelle Wort zur aktuellen Zeile hinzu
        test_line = current_line + word + ' '

        # Überprüfe, ob die aktuelle Zeile die maximale Breite überschreitet
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            # Füge die aktuelle Zeile zu den gerenderten Zeilen hinzu und starte eine neue Zeile
            rendered_lines.append(current_line)
            current_line = word + ' '

    # Füge die letzte Zeile hinzu
    if current_line:
        rendered_lines.append(current_line)

    # Rendere den Text für jede Zeile und füge ihn zur gerenderten Textoberfläche hinzu
    for line in rendered_lines:
        rendered_text += line.strip() + '\n'

    text_obj = font.render(rendered_text, True, (0, 0, 0))
    padding = 50
    width = text_obj.get_width() + padding
    height = text_obj.get_height() + padding

    #draw the frame around the text ------------------------------------------------
    line_width = 10

    #basic surface
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    #background
    background = pygame.Surface((width-line_width*2, height-line_width*2))
    background.fill((255, 255, 255))
    surface.blit(background, (line_width, line_width))

    #draw the text
    surface.blit(text_obj, (padding//2, padding//2))
        
    #top line
    line = pygame.Surface((width - line_width*2, line_width))
    line.fill((0, 0 ,0))
    surface.blit(line,(line_width, 0))
    
    #left line
    line = pygame.Surface((line_width, height - line_width*2))
    line.fill((0,0,0))
    surface.blit(line,(0, line_width))

    #bottom line
    line = pygame.Surface((width - line_width*2, line_width))
    line.fill((0, 0, 0))
    surface.blit(line,(line_width, height-line_width))
    
    #right line
    line = pygame.Surface((line_width, height - line_width*2))
    line.fill((0,0,0))
    surface.blit(line,(width-line_width, line_width))
    
    #return prepared surface
    return surface



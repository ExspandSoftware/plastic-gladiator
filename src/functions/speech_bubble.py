import pygame

from config import *

def speech_bubble(text, max_width, corner:bool = False, crn_dir:str = "l"):

    # modify the text --------------------------------------------------------------
    font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 32)
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

    text_obj = pygame.Surface((max_width, (font.size(rendered_lines[0])[1])*len(rendered_lines) + 5*(len(rendered_lines)-1)))
    text_obj.fill((255, 255, 255))
    for idx, line in enumerate(rendered_lines):
        line_sf = font.render(rendered_lines[idx], True, (0, 0, 0), (255, 255, 255))
        text_obj.blit(line_sf, (max_width//2 - font.size(rendered_lines[idx])[0]//2, (font.size(rendered_lines[idx])[1] + 5)*idx))
    padding = 50
    width = text_obj.get_width() + padding
    height = text_obj.get_height() + padding

    #draw the frame around the text ------------------------------------------------
    line_width = 10

    #basic surface
    if not corner:
        ext_bot = line_width*0
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
    else:
        ext_bot = line_width*6
        surface = pygame.Surface((width, height + ext_bot), pygame.SRCALPHA)

    #background
    background = pygame.Surface((width-line_width*2, height-line_width*2))
    background.fill((255, 255, 255))
    surface.blit(background, (line_width, line_width))

    #draw the text
    surface.blit(text_obj, (padding//2, padding//2))
    
    #top line
    line = pygame.Surface((width - line_width*4, line_width))
    line.fill((0, 0 ,0))
    surface.blit(line,(line_width*2, 0))

    #top left corner
    cube = pygame.Surface((line_width, line_width))
    cube.fill((0,0,0))
    surface.blit(cube, (line_width, line_width))
    
    #left line
    line = pygame.Surface((line_width, height - line_width*4))
    line.fill((0,0,0))
    surface.blit(line,(0, line_width*2))

    #top right corner
    cube = pygame.Surface((line_width, line_width))
    cube.fill((0,0,0))
    surface.blit(cube, (width - line_width*2, line_width))

    #bottom line
    line = pygame.Surface((width - line_width*4, line_width))
    line.fill((0, 0, 0))
    surface.blit(line,(line_width*2, height-line_width))

    #bottom left corner
    cube = pygame.Surface((line_width, line_width))
    cube.fill((0,0,0))
    surface.blit(cube, (line_width, height - line_width*2))
    
    #right line
    line = pygame.Surface((line_width, height - line_width*4))
    line.fill((0,0,0))
    surface.blit(line,(width-line_width, line_width*2))

    #bottom right corner
    cube = pygame.Surface((line_width, line_width))
    cube.fill((0,0,0))
    surface.blit(cube, (width-line_width*2, height-line_width*2))

    if corner:
        if crn_dir == "l":
            crn_img = pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "comp", "corner_l.png"))
        elif crn_dir == "r":
            crn_img = pygame.image.load(os.path.join(WORKING_DIR, "assets", "images", "comp", "corner_r.png"))
        crn_img = pygame.transform.scale(crn_img, (line_width*7, line_width*7))

        if crn_dir == "l":
            surface.blit(crn_img, (line_width*5, height-line_width))
        elif crn_dir == "r":
            surface.blit(crn_img, (width - line_width*5 - ext_bot, height-line_width))
    
    #return prepared surface
    return surface



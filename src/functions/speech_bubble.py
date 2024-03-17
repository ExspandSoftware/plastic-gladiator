import pygame

from config import *

def speech_bubble(width, height):
    line_width = 10

    #basic surface
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    #background
    background = pygame.Surface((width-line_width*2, height-line_width*2))
    background.fill((255, 255, 255))
    surface.blit(background, (line_width, line_width))
        
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



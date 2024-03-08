import pygame

from config import *

def basic_rect(width, height):
    line_width = 5
    line_height = 5

    #basic surface
    surface = pygame.Surface((width, height))
    surface.fill((174,163,151))
    
    #top line rect 2 
    line = pygame.Surface((width, line_width))
    line.fill((154,146,137))
    surface.blit(line,(line_width, line_height))
    
    #left line rect 2
    line = pygame.Surface((line_width, height))
    line.fill((154,146,137))
    surface.blit(line,(line_width, line_height))

    #right line rect 2
    line = pygame.Surface((line_width, height))
    line.fill((186,174,161))
    surface.blit(line, (width-2*line_width, line_height))

    #bottom line rect 2
    line = pygame.Surface((width - 2*line_width, line_height))
    line.fill((186,174,161))
    surface.blit(line, (line_width, height-2*line_height))

    #top line rect 1
    line = pygame.Surface((width, line_height))
    line.fill((214,200,185))
    surface.blit(line, (0, 0))

    #left line rect 1
    line = pygame.Surface((line_width, height))
    line.fill((214,200,185))
    surface.blit(line, (0, 0))

    #right line rect 1
    line = pygame.Surface((line_width, height))
    line.fill((137,128,118))
    surface.blit(line, (width-line_width, 0))

    #bottom line rect 1
    line = pygame.Surface((width, line_width))
    line.fill((137,128,118))
    surface.blit(line, (0, height-line_height))  

    #return prepared surface
    return surface



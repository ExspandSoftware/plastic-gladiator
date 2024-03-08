import pygame

from config import *

def basic_rect(width, height):
    #basic surface
    surface = pygame.Surface((width, height))

    #first line
    line = pygame.Surface((width, 5))
    line.fill((200, 200, 200))
    surface.blit(line, (0, 0))

    #second line
    line = pygame.Surface((5, height))
    line.fill((200, 200, 200))
    surface.blit(line, (0, 0))

    #third line
    line = pygame.Surface((5, height))
    line.fill((200, 200, 200))
    surface.blit(line, (0, 0))

    #second line
    line = pygame.Surface((5, height))
    line.fill((200, 200, 200))
    surface.blit(line, (0, 0))    
    
    #second line
    line = pygame.Surface((5, height))
    line.fill((200, 200, 200))
    surface.blit(line, (0, 0))
    #return prepared surface
    return surface

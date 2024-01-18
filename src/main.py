import pygame as pg

import sys
import os

# setup frame and game engine
pg.init()
scr = pygame.display.set_mode((1200, 700),pygame.RESIZABLE)
clock = pg.time.Clock()
running = True

# Now set the title for the window
pygame.display.set_caption('')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(30)  # limits FPS to 60

pg.quit()
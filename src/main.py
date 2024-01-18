import pygame as pg

import sys
import os

# setup frame and game engine
pg.init()
scr = pg.display.set_mode((1920, 1080), pg.RESIZABLE)
clock = pg.time.Clock()
running = True

# Now set the title for the window
pg.display.set_caption('{PLACEHOLDER}')

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    
    scr.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(30)  # limits FPS to 60

pg.quit()
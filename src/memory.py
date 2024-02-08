# THIS FILE IS ONLY A TESTING FILE AND WILL BE DELETED LATER
# THIS FILE IS ONLY A TESTING FILE AND WILL BE DELETED LATER
# THIS FILE IS ONLY A TESTING FILE AND WILL BE DELETED LATER

# GAME HAS NO REAL ENGIN CARDS ONLY TURN ON CLICK
# GAME HAS NO REAL ENGIN CARDS ONLY TURN ON CLICK
# GAME HAS NO REAL ENGIN CARDS ONLY TURN ON CLICK


import pygame
import sys

from classes.memory import MemoryGame

pygame.init()

# Initialisiere das Pygame-Fenster
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Memory Game")

cards = [
    ((12, 70, 138), (70, 20, 84)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
    ((12, 70, 138), (70, 20, 84)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
    ((72, 49, 139), (64, 47, 26)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
    ((12, 70, 138), (70, 20, 84)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
    ((12, 70, 138), (70, 20, 84)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
    ((72, 49, 139), (64, 47, 26)),
    ((93, 83, 174), (25, 74, 46)),
    ((83, 27, 169), (57, 42, 85)),
    ((72, 49, 139), (64, 47, 26)),
]

testGame = MemoryGame(0, 0, 800, 600, (40, 40, 40), 60, (123, 123, 123))
testGame.create_board(cards)
testGameGroup = pygame.sprite.Group()
testGameGroup.add(testGame)
card_group = testGame.render()


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for card in card_group:
                    if card.is_clicked(mouse_pos[0], mouse_pos[1]):
                        pass

    # Zeichne den Inhalt des Einstellungsfensters auf den Hauptbildschirm
    
    
    #testGameGroup.draw(screen)
    card_group.draw(screen)

    screen.blit(screen, (screen_size[0], screen_size[1]))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

#%% Imports ----------------------------------------------------------------
import pygame

from game import Game


#%% Functions --------------------------------------------------------------
def main():
    pygame.init()
    
    game = Game()
    game.run()

    pygame.quit()

#%% Run Game ---------------------------------------------------------------
if __name__ == "__main__":
    main()
else:
    print("Plastic-Gladiator is a standalone Game and should not be imported as a module!")
    exit(1)

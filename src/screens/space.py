import pygame
import random
import json


from functions.basic_rect import basic_rect

from classes.minigame_player import MinigamePlayer
from classes.plastic_bag import PlasticBag

from config import *

class Space(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.interface = basic_rect(Iwidth*0.4, Iheight*0.9)

        self.bags_left_background = basic_rect(400, 75)

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.plastic_bags = []
        self.max_bags = 30
        self.bags_left = self.max_bags
        self.bags_cleared = 0
        self.time_before_next_bag = 0
        self.t1 = pygame.time.get_ticks()

        self.running = True

        self.minigame_player = MinigamePlayer(Iwidth//2 - 25, Iheight*0.9 - 25, 50, 50)

        self.correct_sound = pygame.mixer.Sound("./assets/sounds/accomplishment_sound.wav")
        self.wrong_sound = pygame.mixer.Sound("./assets/sounds/wrong_sound.wav")

        self.font = pygame.font.Font(os.path.join(WORKING_DIR, "assets", "fonts", "game-font.ttf"), 55)


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #setting up the interface
        self.image.blit(self.interface, self.interface.get_rect(topleft=(Iwidth//2 - self.interface.get_width()//2, Iheight//2 - self.interface.get_height()//2)))

        """
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.running:
            self._run_game()
        self.image.blit(self.bags_left_background, self.bags_left_background.get_rect(topleft=(Iwidth//2 - 200, 0)))
        bags_left_text = self.font.render(f"Übrige Tüten: {self.bags_left}", True, (255, 255, 255))
        self.image.blit(bags_left_text, bags_left_text.get_rect(center=(Iwidth//2, 40)))
    
    def _run_game(self):
        if len(self.plastic_bags) != 0:
            for bag in self.plastic_bags:
                self.image.blit(bag.image, (bag.rect.x, bag.rect.y + 4 - bag.scale))
                bag.rect = bag.image.get_rect(topleft=(bag.rect.x, bag.rect.y + 4 - bag.scale))

                if bag.rect.y + bag.size > Iheight * 0.95 - 10:
                    self.bags_cleared += 1
                    self.plastic_bags.remove(bag)
                    if self.bags_cleared == self.max_bags:
                        self._finish_game(True)

                if bag.rect.colliderect(self.minigame_player.rect):
                    self._finish_game(False)
        
        if len(self.plastic_bags) < self.max_bags and self.bags_left != 0 and pygame.time.get_ticks() - self.t1 > self.time_before_next_bag:
            self.time_before_next_bag = random.randint(500, 900)
            self.t1 = pygame.time.get_ticks()
            scale = random.randint(1, 3)
            self.plastic_bags.append(PlasticBag(random.randint(int(max(Iwidth*0.3 + 10, self.minigame_player.x - 250)), int(min(Iwidth*0.7 - 10 - 30*scale, self.minigame_player.x + 250))), Iheight*0.05 + 10, scale))
            self.bags_left -= 1

    def _finish_game(self, won:bool):
        self.running = False
        if won:
            pygame.mixer.Channel(1).play(self.correct_sound)
        else:
            pygame.mixer.Channel(1).play(self.wrong_sound)

        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "r") as f:
            data = json.load(f)
            progress = data.get("progress", 0)
            memory_turns = data.get("memory_turns", 0)
            f.close()
        with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "w") as f:
            data = {
                "progress": progress,
                "memory_turns": memory_turns,
                "space_bags_cleared": self.bags_cleared,
            }
            json.dump(data, f, indent=4)


    def reset(self):
        self.running = True
        self.plastic_bags = []
        self.bags_left = self.max_bags
        self.bags_cleared = 0
        self.time_before_next_bag = 0
        self.t1 = 0
        self.minigame_player.reset()

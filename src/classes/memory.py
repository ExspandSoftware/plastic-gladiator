import pygame
import random
import math
import os
import json
import time

from classes.memory_card import MemoryCard

from functions.basic_rect import basic_rect

from config import *

class MemoryGame(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image, card_size: int, default_card_image):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.game_window = basic_rect(width, height)
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.turn_count_background = basic_rect(250, 75)

        self.card_size = card_size
        self.default_card_image = default_card_image
        self.cards = None
        self.clickable_cards = None
        self.card_is_open = False
        self.cards_should_turn = False
        self.opened_card = None
        self.opened_card2 = None
        self.turn_count = 0

        self.font = pygame.font.Font(os.path.join(WORKING_DIR, "assets", "fonts", "game-font.ttf"), 55)
        self.correct_sound = pygame.mixer.Sound("./assets/sounds/accomplishment_sound.wav")
        self.wrong_sound = pygame.mixer.Sound("./assets/sounds/wrong_sound.wav")
    
    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        value = kwargs["game_class"]

        self.image.blit(self.game_window, self.game_window.get_rect(topleft=(self.x, self.y)))
        self.image.blit(self.turn_count_background, self.turn_count_background.get_rect(topleft=(Iwidth//2 - 125, 0)))

        turn_count_text = self.font.render(f"Züge: {str(0) + str(self.turn_count) if self.turn_count < 10 else str(self.turn_count)}", True, (255, 255, 255))
        self.image.blit(turn_count_text, turn_count_text.get_rect(center=(Iwidth//2, 40)))

    
    def create_board(self, cards: list[tuple[tuple[int, int, int], tuple[int, int, int]]]):

        card_list = []
        
        for idx, card_pair in enumerate(cards):
            for card in card_pair:
                card_list.append(MemoryCard(idx, self.card_size, card, self.default_card_image))

        self.cards = card_list

    def render(self) -> pygame.sprite.Group:
        card_group = pygame.sprite.Group()
        self.clickable_cards = self.cards.copy()
        random.shuffle(self.clickable_cards)

        for idx, card in enumerate(self.clickable_cards):
            card.set_position(((self.width - math.ceil(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + (idx % math.ceil(math.sqrt(len(self.cards)))) * 1.1 * self.card_size) + 316, ((self.height - int(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + int(idx//math.ceil(math.sqrt(len(self.cards))) % int(math.sqrt(len(self.cards)))) * 1.1 * self.card_size) + 36)
            card_group.add(card)

        return card_group
    
    def is_clicked(self, pos) -> bool:
        x, y = pos

        for card in self.clickable_cards:
            if card.is_clicked(x, y):
                if self.cards_should_turn:
                    self.cards_should_turn = False
                    self.opened_card.turn()
                    self.opened_card2.turn()
                    self.opened_card = None
                    self.opened_card2 = None
                    return
                elif card == self.opened_card:
                    return
                else:
                    card.turn()
                    if not self.card_is_open:
                        if self.opened_card is not None:
                            self.opened_card.turn()
                            self.opened_card = None
                            if self.opened_card2 is not None:
                                self.opened_card2.turn()
                                self.opened_card2 = None
                            return
                                         
                        self.card_is_open = True
                        self.opened_card = card
                    else:
                        if self.opened_card.id != card.id:
                            if self.turn_count < 99:
                                self.turn_count += 1
                            
                            self.card_is_open = False
                            self.cards_should_turn = True
                            self.opened_card2 = card
                            pygame.mixer.Channel(1).play(self.wrong_sound)
                        else:
                            self.clickable_cards.remove(card)
                            self.clickable_cards.remove(self.opened_card)
                            pygame.mixer.Channel(1).play(self.correct_sound)
                            self.card_is_open = False
                            self.opened_card = None
                            if len(self.clickable_cards) == 0:
                                with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "r") as f:
                                    data = json.load(f)
                                    progress = data.get("progress", 0)
                                    f.close()
                                with open(os.path.join(WORKING_DIR, "JSONs", "GameState.json"), "w") as f:
                                    data = {
                                        "progress": progress,
                                        "memory_turns": self.turn_count
                                    }
                                    json.dump(data, f, indent=4)
        
    def close(self):
        self.turn_count = 0
        self.card_is_open = False
        self.cards_should_turn = False
        self.opened_card = None
        self.opened_card2 = None
        for card in self.cards:
            if card.is_open:
                card.turn()
            

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

        self.image = basic_rect(width, height)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.card_size = card_size
        self.default_card_image = default_card_image
        self.cards = None
        self.clickable_cards = None
        self.card_is_open = False
        self.opened_card = None
        self.opened_card2 = None
        self.turn_count = 0
    
    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        value = kwargs["game_class"]

        trp_sfc = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        trp_sfc.fill((0, 0, 0, 150))
        value.screen.blit(trp_sfc, (0, 0))

    
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
                print(card.id)
                if card == self.opened_card:
                    return
                else:
                    card.turn()
                    if not self.card_is_open:
                        if self.opened_card is not None:
                            self.opened_card.turn()
                        if self.opened_card2 is not None:
                            self.opened_card2.turn()
                        self.card_is_open = True
                        self.opened_card = card
                    else:
                        self.turn_count += 1
                        if self.opened_card.id != card.id:
                            self.card_is_open = False
                            self.opened_card2 = card
                        else:
                            self.clickable_cards.remove(card)
                            self.clickable_cards.remove(self.opened_card)
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
        for card in self.cards:
            if card.is_open:
                card.close()      
            

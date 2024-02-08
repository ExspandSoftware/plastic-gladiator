import pygame
import random
import math

from classes.memory_card import MemoryCard

class MemoryGame(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image, card_size: int, default_card_image):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((width, height))
        self.image.fill(image)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.card_size = card_size
        self.default_card_image = default_card_image
        self.cards = None
        self.card_is_open = False
    
    def update(self):
        return
    
    def create_board(self, cards: list[tuple[tuple[int, int, int], tuple[int, int, int]]]):

        card_list = []
        
        for idx, card_pair in enumerate(cards):
            for card in card_pair:
                card_list.append(MemoryCard(idx, self.card_size, card, self.default_card_image))

        self.cards = card_list

    def render(self) -> pygame.sprite.Group:
        card_group = pygame.sprite.Group()
        #card_group.add(self)
        random.shuffle(self.cards)

        for idx, card in enumerate(self.cards):
            card.set_position(((self.width - math.ceil(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + (idx % math.ceil(math.sqrt(len(self.cards)))) * 1.1 * self.card_size), ((self.height - int(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + int(idx//math.ceil(math.sqrt(len(self.cards))) % int(math.sqrt(len(self.cards)))) * 1.1 * self.card_size))
            card_group.add(card)

        return card_group

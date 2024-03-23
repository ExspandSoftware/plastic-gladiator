import pygame
import random
import math

from classes.memory_card import MemoryCard

from functions.basic_rect import basic_rect

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
        self.card_is_open = False
        self.opened_card = None
    
    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        value = kwargs["game_class"]

        trp_sfc = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        trp_sfc.fill((0, 0, 0, 150))
        value.screen.blit(trp_sfc, (0, 0))

    
    def create_board(self, cards: list[tuple[tuple[int, int, int], tuple[int, int, int]]]):

        card_list = []
        
        for idx, card_pair in enumerate(cards):
            for card in card_pair:
                card_list.append(MemoryCard(idx//2, self.card_size, card, self.default_card_image))

        self.cards = card_list

    def render(self) -> pygame.sprite.Group:
        card_group = pygame.sprite.Group()
        #card_group.add(self)
        random.shuffle(self.cards)

        for idx, card in enumerate(self.cards):
            card.set_position(((self.width - math.ceil(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + (idx % math.ceil(math.sqrt(len(self.cards)))) * 1.1 * self.card_size) + 316, ((self.height - int(math.sqrt(len(self.cards))) * 1.1 * self.card_size + 0.1 * self.card_size)//2 + int(idx//math.ceil(math.sqrt(len(self.cards))) % int(math.sqrt(len(self.cards)))) * 1.1 * self.card_size) + 36)
            card_group.add(card)

        return card_group
    
    def is_clicked(self, pos) -> bool:
        x, y = pos

        for card in self.cards:
            if card.is_clicked(x, y):
                if not self.card_is_open:
                    self.card_is_open = True
                    self.opened_card = card
                else:
                    if card == self.opened_card:
                        return
                    elif self.opened_card.id != card.id:
                        self.card_is_open = False
                        self.opened_card.turn()
                        card.turn()
                        self.opened_card = None
                    else:
                        print("Match")
                        self.cards.remove(card)
                        self.cards.remove(self.opened_card)
                        self.card_is_open = False
                        self.opened_card = None
                    
            

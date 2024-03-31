import pygame

from functions.basic_rect import basic_rect

class MemoryCard(pygame.sprite.Sprite):
    def __init__(self, id: int, card_size: tuple[int, int], image:str):
        super().__init__()

        self.id = id
        self.width = card_size
        self.height = card_size
        self.x = 0
        self.y = 0
        self.is_open = False
        tmp_surface = basic_rect(card_size, card_size)
        tmp_image = pygame.image.load(image)
        tmp_image = pygame.transform.scale(tmp_image, (card_size*0.9, card_size*0.9))
        tmp_surface.blit(tmp_image, (card_size*0.05, card_size*0.05))
        self.topside_image = tmp_surface
        self.backside_image = basic_rect(card_size, card_size)
        self.click_sound = pygame.mixer.Sound("./assets/sounds/button_click.mp3")

        self.image = self.topside_image
        self.rect = self.image.get_rect(topleft=(0, 0))


    def update(self, Iwidth: int, Iheight: int, Cwidth: int, Cheight: int, *vars, **kwargs):
        """
        # Scale object
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        

    def is_clicked(self, x: int, y: int) -> bool:
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            pygame.mixer.Channel(2).play(self.click_sound)
            return True
        else:
            return False
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def turn(self):
        if self.is_open:
            self.image = self.backside_image
        else:
            self.image = self.topside_image
        
        self.is_open = not self.is_open
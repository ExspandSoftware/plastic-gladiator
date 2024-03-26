import pygame

class MemoryCard(pygame.sprite.Sprite):
    def __init__(self, id: int, card_size: tuple[int, int], image, backside_image):
        super().__init__()

        self.id = id
        self.width = card_size
        self.height = card_size
        self.x = 0
        self.y = 0
        self.is_open = False
        self.topside_image = image
        self.backside_image = backside_image

        self.image = pygame.Surface((card_size, card_size))
        self.image.fill(backside_image)
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
            self.image.fill(self.backside_image)
        else:
            self.image.fill(self.topside_image)
        
        self.is_open = not self.is_open
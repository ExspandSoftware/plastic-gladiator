import pygame

from functions.basic_rect import basic_rect

class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image, background:bool = True, sound:bool = True):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if background:
            self.image = basic_rect(width, height)
        else:
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        if type(image) == str:
            self.ground = pygame.image.load(image)
            if background:
                self.ground = pygame.transform.scale(self.ground, (self.width-30, self.height-30))
                self.image.blit(self.ground, (15, 15))
            else:
                self.image = self.ground

        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = sound
        if sound:
            self.click_sound = pygame.mixer.Sound("./assets/sounds/button_click.mp3")


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *vars, **kwargs):

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

        #tone button if mouse hovers it
        #if self._mouse_is_over_button(pygame.mouse.get_pos()):
        #    semi_black_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        #    semi_black_surface.fill((255, 255, 255, 10))
        #    self.image.blit(semi_black_surface, (0, 0))

    def is_clicked(self, pos: list[int, int], is_clickable: bool = True):
        if self._mouse_is_over_button(pos) and is_clickable:
            if self.sound:
                pygame.mixer.Channel(2).play(self.click_sound)
            return True
        else:
            return False
        
    def _mouse_is_over_button(self, pos: list[int, int]):
        if pos[0] >= self.rect.x and pos[0] <= self.rect.x + self.image.get_width() and pos[1] >= self.rect.y and pos[1] <= self.rect.y + self.image.get_height():
            return True
        else:
            return False
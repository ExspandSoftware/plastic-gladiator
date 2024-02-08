import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((width, height))
        self.image.fill(image)

        self.rect = self.image.get_rect(topleft=(x, y))

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
        #    semi_black_surface.fill((100, 100, 100, 10))
        #    self.image.blit(semi_black_surface, (0, 0))

    def is_clicked(self, pos: list[int, int], is_clickable: bool = True):
        if self._mouse_is_over_button(pos) and is_clickable:
            pygame.mixer.Sound.play(self.click_sound)
            return True
        else:
            return False
        
    def _mouse_is_over_button(self, pos: list[int, int]):
        if pos[0] >= self.rect.x and pos[0] <= self.rect.x + self.image.get_width() and pos[1] >= self.rect.y and pos[1] <= self.rect.y + self.image.get_height():
            return True
        else:
            return False
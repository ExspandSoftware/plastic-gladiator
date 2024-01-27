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

        self.click_sound = pygame.mixer.Sound("assets/sounds/button_click.mp3")


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *vars, **kwargs):
        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

    def is_clicked(self, pos):
        if pos[0] >= self.rect.x and pos[0] <= self.rect.x + self.image.get_width() and pos[1] >= self.rect.y and pos[1] <= self.rect.y + self.image.get_height():
            pygame.mixer.Sound.play(self.click_sound)
            return True	
        else:
            return False
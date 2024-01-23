import pygame


class GImage(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image):
        super().__init__()

        self.x = x / 1280
        self.y = y / 720
        self.width = width / 1280
        self.height = height / 720

        self.image_store = image
        self.image = pygame.Surface((width, height))
        self.image.fill(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self, *vars, **kwargs):
        for key, value in kwargs.items():
            if key == "width":
                self.image = pygame.Surface((self.width * value, self.image.get_height()))
                self.image.fill(self.image_store)
                self.rect.x = self.x * value
            if key == "height":
                self.image = pygame.Surface((self.image.get_width(), self.height * value))
                self.image.fill(self.image_store)
                self.rect.y = self.y * value
        return

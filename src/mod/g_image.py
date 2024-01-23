import pygame


class GImage(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image):
        super().__init__()

        self.image = pygame.Surface((w, h))
        self.image.fill(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self, stage, *vars, **kwargs):
        return

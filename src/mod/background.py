import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()

        self.image = pygame.Surface((w, h))
        self.image.fill((127, 153, 172))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


    def update(self):
        return

import pygame

class PlasticBag(pygame.sprite.Sprite):

    def __init__(self, x:int, y:int):
        super().__init__()

        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args, **kwargs):
        pass
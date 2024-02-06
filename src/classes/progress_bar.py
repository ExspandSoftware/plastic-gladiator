import pygame

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((width, height))
        self.image.fill(image)
        self.rect = self.image.get_rect(topleft=(x, y))


    def update(self, Iwidth: int, Iheight: int, Cwidth: int, Cheight: int, *vars, **kwargs) -> None:
        # Scale object
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

    def add_progress(self, amount: int) -> None:
        if (self.height + amount) < 5:
            amount = -self.height + 5
        self.y -= amount
        self.height += amount

    def set_progress(self, progress: int) -> None:
        if progress < 5:
            progress = 5
        self.y += (self.height - progress)
        self.height = progress
        
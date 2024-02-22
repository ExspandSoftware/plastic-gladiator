import pygame

class BookScreen(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, page_image):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        
        # other vars
        self.background = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 150))

        self.book_page = pygame.Surface((self.width*0.35, self.height*0.95))
        self.book_page.fill((120, 230, 40))

        self.background.blit(self.book_page, self.book_page.get_rect(topleft=(int(self.x+self.width*0.5), self.height*0.025)))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        # Scale objects
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))
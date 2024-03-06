import pygame

from config import *

class CandyCrush(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = 0
        self.y = 0

        self.width = Iwidth
        self.height = Iheight
        
        # other vars
        self.ground = pygame.Surface((400, 600))
        self.ground.fill((45, 45, 45))

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        #vars for the game
        self.cells_axis = 6

        self.font = pygame.font.Font(os.path.join(WORKING_DIR, 'assets', 'fonts', 'game-font.ttf'), 100)


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):

        #handle the time for the game, after 45 sec. it should be closed automatically
        self.handle_timer(kwargs)

        #draw the game
        self.draw_game()

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))


    def draw_game(self):
        #setting up the interface
        ground_x = Iwidth*0.5-self.ground.get_width()//2
        ground_y = Iheight*0.5-self.ground.get_height()//2

        self.image.blit(self.ground, self.ground.get_rect(topleft=(Iwidth*0.5-self.ground.get_width()//2, Iheight*0.5-self.ground.get_height()//2)))
        pygame.draw.rect(self.image, '#c0c0c2', pygame.Rect(ground_x, ground_y - 10, self.ground.get_width(), 10))
        pygame.draw.rect(self.image, '#c0c0c2', pygame.Rect(ground_x, ground_y + self.ground.get_height(), self.ground.get_width(), 10))
        pygame.draw.rect(self.image, '#c0c0c2', pygame.Rect(ground_x - 10, ground_y, 10, self.ground.get_height()))
        pygame.draw.rect(self.image, '#c0c0c2', pygame.Rect(ground_x + self.ground.get_width(), ground_y, 10, self.ground.get_height()))

        #draw the game surface
        game_x = ground_x + 10
        game_y = ground_y + self.ground.get_height() - self.ground.get_width() + 10
        game_width = self.ground.get_width() - 20
        pygame.draw.rect(self.image, '#828385', pygame.Rect(game_x-2, game_y-2, game_width+5, game_width+5))
        cell_width = game_width//self.cells_axis
        for i in range(self.cells_axis):
            for j in range(self.cells_axis):
                pygame.draw.rect(self.image, '#565656', pygame.Rect(game_x + cell_width*i + (i+1), game_y + cell_width*j + (j+1), cell_width-4, cell_width-4))

        #draw the right time ontop of the game screen
        seconds_txt = self.timer
        if self.timer <= 9:
            seconds_txt = "0"+str(seconds_txt)
        else:
            seconds_txt = str(seconds_txt)
        timer_text = self.font.render("00:"+seconds_txt, True, (255, 255, 255))
        self.image.blit(timer_text, (self.width//2 - timer_text.get_width()//2, ground_y + (game_y-ground_y)//2 - timer_text.get_height()//2))

    def handle_timer(self, kwargs):
        #handle the time for the game, after 45 sec. it should be closed automatically
        self.timer = (21000 - (pygame.time.get_ticks() - self.start_time))//1000
        if self.timer == 0:
            for key, value in kwargs.items():
                if key == "game_class":
                    value.pre_edeka_buttons_pressable = True
                    value.movement = True
                    value.active_sprites.remove(value.candy_crush_game)
                    value.active_sprites.remove(value.close_button)     
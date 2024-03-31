import pygame
import random

from config import *
from functions.speech_bubble import speech_bubble


class Candy(pygame.sprite.Sprite):
    id: int
    x_pos: int
    y_pos: int

    is_selected: bool = False

    width: int = 50
    height: int = 50

    image: pygame.Surface
    image_file_path: str
    rect: pygame.Rect

    def __init__(self, id: int, x_pos: int, y_pos: int, image_file_path: str):
        super().__init__()

        self.id = id
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image_file_path = image_file_path

        self.image = pygame.image.load(image_file_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
    
    def __str__(self):
        return f"Candy {self.id} at ({self.x_pos}, {self.y_pos})"
    
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x_pos, self.y_pos))
    
    def update(self, *args, **kwargs):
        pass

    def copy(self):
        return Candy(self.id, self.x_pos, self.y_pos, self.image_file_path)

        


class CandyCrush(pygame.sprite.Sprite):
    x: int = 0
    y: int = 0

    cells_axis: int = 6

    score: int = 0

    height: int = Iheight
    width: int = Iwidth

    ground: pygame.Surface
    image: pygame.Surface
    rect: pygame.Rect
    start_time: int
    font: pygame.font.Font


    board_state: list[list[Candy]] = []

    selected_positions: list[tuple[int, int]] = []


    def __init__(self):
        super().__init__()

        self.ground = pygame.Surface((400, 600))
        self.ground.fill((45, 45, 45))

        self.image = pygame.Surface((Iwidth, Iheight), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 150))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.font = pygame.font.Font(os.path.join(WORKING_DIR, "assets", "fonts", "game-font.ttf"), 100)

        # fill board state with Candy objects
        candy_options = [
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Glasflasche-mit-Pfand.png"),
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Glasflasche-ohne-Pfand.png"),
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Pappbecher-1.png"),
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Pappbecher-2.png"),
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Plastik-Flasche-mit-Pfand.png"),
            os.path.join(WORKING_DIR, "assets", "images", "pre_edeka", "candy_crush", "Plastik-Flasche-ohne-Pfand.png"),
        ]
        board_state = [[
            [0, 1, 2, 4, 4, 5],
            [0, 1, 4, 4, 1, 5],
            [3, 0, 2, 4, 3, 1],
            [5, 1, 2, 3, 0, 2],
            [1, 5, 0, 0, 1, 5],
            [3, 1, 2, 3, 2, 3],
        ],[
            [0, 1, 2, 4, 4, 5],
            [0, 1, 4, 4, 1, 5],
            [3, 0, 2, 4, 3, 1],
            [5, 1, 2, 3, 0, 2],
            [1, 5, 0, 0, 1, 5],
            [3, 1, 2, 3, 2, 3],
        ],[
            [0, 1, 2, 4, 4, 5],
            [0, 1, 4, 4, 1, 5],
            [3, 0, 2, 4, 3, 1],
            [5, 1, 2, 3, 0, 2],
            [1, 5, 0, 0, 1, 5],
            [3, 1, 2, 3, 2, 3],
        ]]
        board_idx = random.randint(0, len(board_state) - 1)

        for i in range(self.cells_axis):
            row = []
            for j in range(self.cells_axis):
                idx = board_state[board_idx][i][j]
                candy = Candy(idx, 0, 0, candy_options[idx])

                candy.x_pos = Iwidth*0.5-self.ground.get_width()//2 + 10 + (self.ground.get_width() - 20)//self.cells_axis*i + (i+1)
                candy.y_pos = Iheight*0.5-self.ground.get_height()//2 + self.ground.get_height() - self.ground.get_width() + 10 + (self.ground.get_width() - 20)//self.cells_axis*j + (j+1)

                row.append(candy)
            self.board_state.append(row)
        
        self.start_time = pygame.time.get_ticks()
        self.saved_bottles = 6




    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):

        #clear the screen
        self.image.fill((0, 0, 0, 150))

        #handle the time for the game, after 45 sec. it should be closed automatically
        self.time_since_start_ms = pygame.time.get_ticks() - self.start_time


        #structure the time whenm the window was opened
        self.interval_1_ms = 8000
        self.interval_2_ms = 45000
        self.interval_3_ms = 10000
        self.interval_4_ms = 10000
        if 0 <= self.time_since_start_ms <= self.interval_1_ms:
            sb = speech_bubble("Sehr gut! Wie es aussieht, hat jemand einige Pfandflaschen im Muelleimer vergessen... Sammle die Pfandflaschen und bringe sie zum Pfandautomaten im Eingang des Supermarktes! Viel Erfolg, dir bleibt nicht viel Zeit... (Du erkennst eine Pfandflasche an dem Pfandsymbol auf dem Etikette.)", 500, True, "r")
            self.image.blit(sb, (Iwidth//2 - sb.get_width()//2, Iheight//2 - sb.get_height()//2))
        elif self.interval_1_ms <= self.time_since_start_ms <= self.interval_1_ms + self.interval_2_ms:
            #draw the game
            self.draw_game()
        elif self.interval_1_ms + self.interval_2_ms <= self.time_since_start_ms <= self.interval_1_ms + self.interval_2_ms + self.interval_3_ms:
            with open(os.path.join(WORKING_DIR, "assets", "data", "note_1.txt"), 'r') as file:
                text = file.read()
            sb = speech_bubble(text, 650, True, "r")
            self.image.blit(sb, (Iwidth//2 - sb.get_width()//2, Iheight//2 - sb.get_height()//2))
        elif self.interval_1_ms + self.interval_2_ms + self.interval_3_ms <= self.time_since_start_ms <= self.interval_1_ms + self.interval_2_ms + self.interval_3_ms + self.interval_4_ms:
            with open(os.path.join(WORKING_DIR, "assets", "data", "note_2.txt"), 'r') as file:
                text = file.read()
            sb = speech_bubble(text, 650, True, "r")
            self.image.blit(sb, (Iwidth//2 - sb.get_width()//2, Iheight//2 - sb.get_height()//2))
        elif self.time_since_start_ms >= self.interval_1_ms + self.interval_2_ms:
            #close the window automatically after the time has finished
            if "game_class" in kwargs:
                value = kwargs["game_class"]
                value.pre_edeka_buttons_pressable = True
                value.movement = True
                value.active_sprites.remove(value.candy_crush_game)
                value.active_sprites.remove(value.close_button)
                value.inventory_screen.items[0][1] += self.saved_bottles
                value.secret_progress = 0.2

        """
        # scale the image to the window size
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight


        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        """
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def draw_game(self):
        #setting up the interface
        ground_x = Iwidth*0.5-self.ground.get_width()//2
        ground_y = Iheight*0.5-self.ground.get_height()//2

        self.image.blit(self.ground, self.ground.get_rect(topleft=(Iwidth*0.5-self.ground.get_width()//2, Iheight*0.5-self.ground.get_height()//2)))
        pygame.draw.rect(self.image, "#c0c0c2", pygame.Rect(ground_x, ground_y - 10, self.ground.get_width(), 10))
        pygame.draw.rect(self.image, "#c0c0c2", pygame.Rect(ground_x, ground_y + self.ground.get_height(), self.ground.get_width(), 10))
        pygame.draw.rect(self.image, "#c0c0c2", pygame.Rect(ground_x - 10, ground_y, 10, self.ground.get_height()))
        pygame.draw.rect(self.image, "#c0c0c2", pygame.Rect(ground_x + self.ground.get_width(), ground_y, 10, self.ground.get_height()))

        #draw the game surface
        game_x = ground_x + 10
        game_y = ground_y + self.ground.get_height() - self.ground.get_width() + 10
        game_width = self.ground.get_width() - 20
        pygame.draw.rect(self.image, "#828385", pygame.Rect(game_x-2, game_y-2, game_width+5, game_width+5))
        cell_width = game_width//self.cells_axis
        for i in range(self.cells_axis):
            for j in range(self.cells_axis):
                pygame.draw.rect(self.image, "#565656", pygame.Rect(game_x + cell_width*i + (i+1), game_y + cell_width*j + (j+1), cell_width-4, cell_width-4))

        #draw the right time ontop of the game screen
        seconds_txt = ((self.interval_1_ms + self.interval_2_ms) - (pygame.time.get_ticks() - self.start_time))//1000
        if seconds_txt < 10:
            seconds_txt = f"0{seconds_txt}"
        else:
            seconds_txt = str(seconds_txt)

        timer_text = self.font.render(f"00:{seconds_txt}", True, (255, 255, 255))
        self.image.blit(timer_text, (self.width//2 - timer_text.get_width()//2, ground_y + (game_y-ground_y)//2 - timer_text.get_height()//2))

        
        # update candies
        for i in range(self.cells_axis):
            for j in range(self.cells_axis):
                candy = self.board_state[i][j]
                candy.update()
                candy.draw(self.image)
        
        return
    
    def pos_to_grid(self, x: int, y: int):
        # convert mouse position to grid position
        game_x = Iwidth*0.5-self.ground.get_width()//2 + 10
        game_y = Iheight*0.5-self.ground.get_height()//2 + self.ground.get_height() - self.ground.get_width() + 10
        game_width = self.ground.get_width() - 20
        cell_width = game_width//self.cells_axis

        if x < game_x or x > game_x + game_width or y < game_y or y > game_y + game_width:
            return None
        
        grid_x = (x - game_x)//cell_width
        grid_y = (y - game_y)//cell_width

        return (grid_x, grid_y)
    
    def check_triple(self, board_state = None) -> bool:
        if board_state is None:
            board_state = self.board_state
        
        for x in range(self.cells_axis - 2):
            x = x + 1
            for y in range(self.cells_axis - 2):
                y = y + 1
                # check sorounding 3x3 grid
                if board_state[x][y].id == board_state[x-1][y].id == board_state[x+1][y].id:
                    return True
                if board_state[x][y].id == board_state[x][y-1].id == board_state[x][y+1].id:
                    return True
        return False
    

    def handle_triplets(self):
        # handle when we know there is at least one triplet in self.board_state
        # remove the triplets and fill the board
        # the three removed cells will be filled by gravity from the top
        # at the top, we generate new candies

        # remove triplets
        for x in range(self.cells_axis - 2):
            x = x + 1
            for y in range(self.cells_axis - 2):
                y = y + 1
                # check sorounding 3x3 grid
                if self.board_state[x][y].id == self.board_state[x-1][y].id == self.board_state[x+1][y].id:
                    self.board_state[x][y].id = -1
                    self.board_state[x-1][y].id = -1
                    self.board_state[x+1][y].id = -1
                if self.board_state[x][y].id == self.board_state[x][y-1].id == self.board_state[x][y+1].id:
                    self.board_state[x][y].id = -1
                    self.board_state[x][y-1].id = -1
                    self.board_state[x][y+1].id = -1

        # fill the board
        for x in range(self.cells_axis):
            for y in range(self.cells_axis):
                if self.board_state[x][y].id == -1:
                    for y_above in range(y, 0, -1):
                        self.board_state[x][y_above].id = self.board_state[x][y_above-1].id
                    new_candy_id = random.randint(0, 4)
                    self.board_state[x][0].id = new_candy_id
                    self.board_state[x][0].image = pygame.image.load(self.board_state[x][0].image_file_path)
                    self.board_state[x][0].image = pygame.transform.scale(self.board_state[x][0].image, (self.board_state[x][0].width, self.board_state[x][0].height))
                    self.board_state[x][0].id = new_candy_id

        return        

    

    def handle_click(self, x: int, y: int):
        # handle the click on the game
        grid_pos = self.pos_to_grid(x, y)
        if grid_pos is None:
            return
        
        if len(self.selected_positions) == 2:
            # two are already selected
            for pos in self.selected_positions:
                self.board_state[pos[0]][pos[1]].is_selected = False
            self.selected_positions = []
        
        self.selected_positions.append(grid_pos)

        if len(self.selected_positions) == 1:
            self.board_state[grid_pos[0]][grid_pos[1]].is_selected = True
            return
        
        # two are selected.
        # check if swapping them would lead to a triple
        # if yes, swap them

        pos1 = self.selected_positions[0]
        pos2 = self.selected_positions[1]

        if abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) != 1: # not adjacent
            return
        
        #swapp them
        swapped_board = self.board_state.copy()
        swapped_board[pos1[0]][pos1[1]], swapped_board[pos2[0]][pos2[1]] = swapped_board[pos2[0]][pos2[1]], swapped_board[pos1[0]][pos1[1]]

        if self.check_triple(swapped_board):
            # there is a legal move, so we swap them
            self.board_state[pos1[0]][pos1[1]], self.board_state[pos2[0]][pos2[1]] = self.board_state[pos2[0]][pos2[1]], self.board_state[pos1[0]][pos1[1]]
            self.selected_positions = []
        else:
            # no legal move, so we deselect them
            for pos in self.selected_positions:
                self.board_state[pos[0]][pos[1]].is_selected = False
            self.selected_positions = []
        
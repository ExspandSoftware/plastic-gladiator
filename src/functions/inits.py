from classes.player import Player
from classes.button import Button
from classes.g_image import GImage
from classes.progress_bar import ProgressBar

from screens.book_screen import BookScreen
from screens.settings_screen import SettingsScreen
from screens.inventory import Inventory
from screens.candy_crush import CandyCrush
from screens.deposit_machine import DepositeMachine
from screens.memory import Memory
from screens.space import Space

from config import *

def init_home(self):
    #init variables for the home page
    self.whoosh_sound = pygame.mixer.Sound("./assets/sounds/slow-whoosh.mp3")
    self.scroll_sound = pygame.mixer.Sound("./assets/sounds/scroll_paper.mp3")

    #pop-up screens
    self.home_buttons_pressable = True
    self.next_page_pressable = False
    self.last_page_pressable = False

    #load images from assets from home folder
    def load_image_asset(subfolder, file):
        if subfolder is not None:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'home', subfolder, file)
        else:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'home', file)
    
    # objects in the stage
    self.home_background        = GImage(0, 0, Iwidth, Iheight, load_image_asset('components', 'background.jpg'))
    self.titel_name             = GImage(Iwidth//2 - int(Iwidth*0.2), int(Iheight*0.02), int(Iwidth*0.4), int(Iheight*0.25), (123, 65, 235))
    self.player                 = Player(Iwidth//2 - Iwidth//12, int(Iheight * 0.333), Iwidth//6, Iheight*0.6)
    self.progress_bar           = ProgressBar(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.16), int(Iheight*0.6))
    self.settings_button        = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), load_image_asset('buttons', 'settings-button.png'))
    self.start_button           = Button(int(Iwidth*0.6675), int(Iheight*0.7675), int(Iwidth*0.3125), int(Iheight*0.2125), load_image_asset('buttons', 'Start-button.png'))
    self.book                   = Button(int(Iwidth*0.02), int(Iheight*0.98 - int(Iwidth*0.1)), int(Iwidth*0.1), int(Iwidth*0.1), (176, 23, 205))

    #sprites for the book
    self.book_cover             = GImage(int(Iwidth*0.5- Iheight*0.32), int(Iheight*0.1),  int(Iheight*0.64), int(Iheight*0.8), load_image_asset('book', 'Buch-Cover-mit-Titel.png'))
    self.page1                  = GImage(int(Iwidth * 0.1), int(Iheight * 0.1), int(Iwidth * 0.8), int(Iheight * 0.8), (123, 45, 67))
    self.page2                  = GImage(int(Iwidth * 0.1), int(Iheight * 0.1), int(Iwidth * 0.8), int(Iheight * 0.8), (45, 67, 123))
    self.page3                  = GImage(int(Iwidth * 0.1), int(Iheight * 0.1), int(Iwidth * 0.8), int(Iheight * 0.8), (67, 123, 45))
    self.pages                  = [self.book_cover, self.page1, self.page2, self.page3]
    self.book_screen            = BookScreen(0, 0, Iwidth, Iheight, (123, 93, 235), self.pages, 0)
    self.next_page              = Button(Iwidth - 140, Iheight/2 - 70, 140, 140, load_image_asset('buttons', 'arrow_right.png'), False)
    self.last_page              = Button(0, Iheight/2 - 70, 140, 140, load_image_asset('buttons', 'arrow_left.png'), False)
    self.close_button           = Button(Iwidth - 50 - Iheight*0.025, Iheight*0.025, 50, 50, load_image_asset('buttons', 'close-button.png'))

    #sprites for the settings screen
    self.settings_screen        = SettingsScreen()

    #add those objects to the right sprites group
    self.active_sprites.add(self.home_background)
    self.active_sprites.add(self.player)
    self.active_sprites.add(self.titel_name)
    self.active_sprites.add(self.progress_bar)
    self.active_sprites.add(self.settings_button)
    self.active_sprites.add(self.start_button)
    self.active_sprites.add(self.book)


def init_pre_edeka(self):
    #pop-up screens
    self.pre_edeka_buttons_pressable = True

    #load images from assets from home folder
    def load_image_asset(subfolder, file):
        if subfolder is not None:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'pre_edeka', subfolder, file)
        else:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'pre_edeka', file)

    # objects in the stage
    self.edeka_background       = GImage(0, 0, Iwidth, Iheight, (15, 65, 34))
    self.player                 = Player(int(Iwidth*0.1), -100, Iwidth//15, Iheight*0.23)
    self.door_L                 = GImage(int(Iwidth*0.65), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))
    self.door_R                 = GImage(int(Iwidth*0.75), int(Iheight*0.4), int(Iwidth*0.1), int(Iheight*0.3) + Iheight//5, (178, 143, 12))
    self.secret_background      = GImage(Iwidth, 0, Iwidth, Iheight, (15*2, 65*2, 34*2))
    self.secret_button_bin      = Button(Iwidth + int(Iwidth*0.75), int(Iheight*0.7 + Iheight//5 - Iheight//7.5), Iwidth//20, Iheight//7.5, (100, 100, 120))
    self.settings_button        = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), load_image_asset('buttons', 'settings-button.png'))
    self.inventory_button       = Button(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (12, 215, 165))

    #sprites for the pop-up screen
    self.settings_screen        = SettingsScreen()
    self.inventory_screen       = Inventory()
    self.close_button           = Button(Iwidth - 50 - Iheight*0.025, Iheight*0.025, 50, 50, load_image_asset('buttons', 'close-button.png'))

    #minigame
    self.candy_crush_game       = CandyCrush()

    #add those objects to the right sprites group
    self.active_sprites.add(self.edeka_background)
    self.active_sprites.add(self.door_L)
    self.active_sprites.add(self.door_R)
    self.active_sprites.add(self.secret_background)
    self.active_sprites.add(self.secret_button_bin)
    self.active_sprites.add(self.settings_button)
    self.active_sprites.add(self.inventory_button)
    self.active_sprites.add(self.player)


def init_edeka(self):
    #pop-up screens
    self.edeka_buttons_pressable = True

    #load images from assets from home folder
    def load_image_asset(subfolder, file):
        if subfolder is not None:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', subfolder, file)
        else:
            return os.path.join(WORKING_DIR, 'assets', 'images', 'edeka', file)

    # objects in stage 1
    self.edeka_1_background         = GImage(0, 0, Iwidth, Iheight, (123, 53, 12))
    self.deposit_machine_button     = Button(200, 150, 220, 520, load_image_asset('components', 'Pfandautomat.png'))
    self.deposit_machine_image      = GImage(420, 150, 220, 520, load_image_asset('components', 'Pfandautomat.png'))
    self.deposit_machine            = DepositeMachine(load_image_asset('components', 'Pfandautomat.png'))

    # obejcts in stage 2
    self.edeka_2_background         = GImage(0, 0, Iwidth, Iheight, load_image_asset('backgrounds', 'Suessigkeitentheke.png'))
    self.memory_button              = Button(Iwidth//2 - 50, Iheight//2 - 50, 100, 100, (192, 160, 236))
    self.memory_game                = Memory()
                    
    # obejcts in stage 3
    self.edeka_3_background         = GImage(0, 0, Iwidth, Iheight, load_image_asset('backgrounds', 'Fleischtheke.png'))
    self.space_button               = Button(Iwidth//2 - 50, Iheight//2 - 50, 100, 100, (192, 160, 236))
    self.space                      = Space()      

    # obejcts in stage 4
    self.edeka_4_background         = GImage(0, 0, Iwidth, Iheight, (12, 253, 123))

    #general objects needed for the stage
    self.settings_button            = Button(int(Iwidth*0.88), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), load_image_asset('buttons', 'settings-button.png'))
    self.inventory_button           = Button(int(Iwidth*0.02), int(Iheight*0.02), int(Iwidth*0.1), int(Iwidth*0.1), (12, 215, 165))
    self.settings_screen            = SettingsScreen()
    self.inventory_screen           = Inventory()
    self.close_button               = Button(Iwidth - 50 - Iheight*0.025, Iheight*0.025, 50, 50, load_image_asset('buttons', 'close-button.png'))
    self.player                     = Player(int(Iwidth*0.1), int(Iheight*0.5), Iwidth//7, Iheight//2)

    # add those objects to the right sprites group
    add_edeka_1(self)
    add_general(self)

def add_general(self):
    self.active_sprites.add(self.settings_button)
    self.active_sprites.add(self.inventory_button)
    self.active_sprites.add(self.player)
def add_edeka_1(self):
    # add those objects to the right sprites group
    self.active_sprites.add(self.edeka_1_background)
    self.active_sprites.add(self.deposit_machine_button)
    self.active_sprites.add(self.deposit_machine_image)
def add_edeka_2(self):
    # add those objects to the right sprites group
    self.active_sprites.add(self.edeka_2_background)
    self.active_sprites.add(self.memory_button)
def add_edeka_3(self):
    # add those objects to the right sprites group
    self.active_sprites.add(self.edeka_3_background)
    self.active_sprites.add(self.space_button)
def add_edeka_4(self):
    # add those objects to the right sprites group
    self.active_sprites.add(self.edeka_4_background)
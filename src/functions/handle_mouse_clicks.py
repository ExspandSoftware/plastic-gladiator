import pygame

from config import *


def handle_mouse_home(self, event):

    #start button ---------------------------------------------------------------------------------
    if self.start_button.is_clicked(event.pos, self.home_buttons_pressable):
        pygame.mixer.Sound.play(self.whoosh_sound)
        self.tmp_ticker_start = pygame.time.get_ticks()
        self.black_transition = (True, "walk_into_edeka")
        self.home_buttons_pressable = False
        self.transition_player_info = [int(Iwidth*0.05), -100, Iwidth//15, Iheight//5]
        
        if self.progress < 0.2:
            self.progress = 0.2

    #settings button ------------------------------------------------------------------------------
    if self.settings_button.is_clicked(event.pos, self.home_buttons_pressable):
        
        self.home_buttons_pressable = False
        self.show_settings = True

        self.active_sprites.add(self.settings_screen)
        self.active_sprites.add(self.close_button)

    if self.show_settings:
        
        if self.close_button.is_clicked(event.pos, self.show_settings):
            self.home_buttons_pressable = True
            self.show_settings = False

            self.active_sprites.remove(self.close_button)
            self.active_sprites.remove(self.settings_screen)

    #book button ----------------------------------------------------------------------------------
    if self.book.is_clicked(event.pos, self.home_buttons_pressable):
        self.home_buttons_pressable = False
        self.active_sprites.add(self.book_screen)
        self.active_sprites.add(self.close_button)
        self.active_sprites.add(self.pages[self.book_screen.current_page])
        self.show_book = True

        if len(self.book_screen.pages) - 1 == self.book_screen.current_page:
            self.next_page_pressable = False
        else: 
            self.active_sprites.add(self.next_page)
            self.next_page_pressable = True

        if self.book_screen.current_page == 0:
            self.last_page_pressable = False
        else:
            self.active_sprites.add(self.last_page)
            self.last_page_pressable = True

    if self.show_book:
        if self.next_page.is_clicked(event.pos, self.next_page_pressable):
            pygame.mixer.Sound.play(self.scroll_sound)
            self.active_sprites.remove(self.pages[self.book_screen.current_page])
            self.book_screen.current_page += 1
            self.active_sprites.add(self.pages[self.book_screen.current_page])
            if len(self.book_screen.pages) - 1 == self.book_screen.current_page:
                self.active_sprites.remove(self.next_page)
                self.next_page_pressable = False
            if self.book_screen.current_page == 1:
                self.active_sprites.add(self.last_page)
                self.last_page_pressable = True

        if self.last_page.is_clicked(event.pos, self.last_page_pressable):
            pygame.mixer.Sound.play(self.scroll_sound)
            self.active_sprites.remove(self.pages[self.book_screen.current_page])
            self.book_screen.current_page += -1
            self.active_sprites.add(self.pages[self.book_screen.current_page])
            if self.book_screen.current_page == 0:
                self.active_sprites.remove(self.last_page)
                self.last_page_pressable = False
            if self.book_screen.current_page == len(self.book_screen.pages) - 2:
                self.active_sprites.add(self.next_page)
                self.next_page_pressable = True
        
        if self.close_button.is_clicked(event.pos, self.show_book):
            self.home_buttons_pressable = True
            self.active_sprites.remove(self.pages[self.book_screen.current_page])
            self.active_sprites.remove(self.book_screen)
            self.active_sprites.remove(self.next_page)
            self.active_sprites.remove(self.last_page)
            self.active_sprites.remove(self.close_button)
            self.show_book = False


def handle_mouse_pre_edeka(self, event):

    # open the minigame window
    if self.secret_button_bin.is_clicked(event.pos, self.pre_edeka_buttons_pressable):
        self.pre_edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.candy_crush_game)
        self.active_sprites.add(self.close_button)

        self.candy_crush_game.start_time = pygame.time.get_ticks()

    #settings button ------------------------------------------------------------------------------
    if self.settings_button.is_clicked(event.pos, self.pre_edeka_buttons_pressable):
        
        self.pre_edeka_buttons_pressable = False
        self.show_settings = True
        self.movement = False

        self.active_sprites.add(self.settings_screen)
        self.active_sprites.add(self.close_button)

    #inventory button -----------------------------------------------------------------------------
    if self.inventory_button.is_clicked(event.pos, self.pre_edeka_buttons_pressable):
        
        self.pre_edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.inventory_screen)
        self.active_sprites.add(self.close_button)

    #close all pop-up-screens
    if not self.pre_edeka_buttons_pressable:    
        if self.close_button.is_clicked(event.pos, not self.pre_edeka_buttons_pressable):

            self.pre_edeka_buttons_pressable = True
            self.movement = True

            self.active_sprites.remove(self.close_button)
            self.active_sprites.remove(self.inventory_screen)
            self.active_sprites.remove(self.settings_screen)
            self.active_sprites.remove(self.candy_crush_game)


def handle_mouse_edeka(self, event):
    
    #stage 1 --------------------------------------------------------------------------------------
    # open the minigame window
    if self.deposit_machine_button.is_clicked(event.pos, self.edeka_buttons_pressable):
        self.edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.deposit_machine)
        self.active_sprites.add(self.close_button)

    
    #stage 2 --------------------------------------------------------------------------------------
    # open the minigame window
    if self.memory_button.is_clicked(event.pos, self.edeka_buttons_pressable):
        self.edeka_buttons_pressable = False
        self.movement = False


        self.memory_game.create_board(self.cards)

        self.active_sprites.add(self.memory_game)
        self.rendered_cards = self.memory_game.render()
        self.active_sprites.add(self.rendered_cards)

        self.active_sprites.add(self.close_button)

    #stage 3 --------------------------------------------------------------------------------------
    # open the minigame window
    if self.space_button.is_clicked(event.pos, self.edeka_buttons_pressable):
        self.edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.space)
        self.active_sprites.add(self.close_button)

    #settings button ------------------------------------------------------------------------------
    if self.settings_button.is_clicked(event.pos, self.edeka_buttons_pressable):
        
        self.edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.settings_screen)
        self.active_sprites.add(self.close_button)

    #inventory button -----------------------------------------------------------------------------
    if self.inventory_button.is_clicked(event.pos, self.edeka_buttons_pressable):
        
        self.edeka_buttons_pressable = False
        self.movement = False

        self.active_sprites.add(self.inventory_screen)
        self.active_sprites.add(self.close_button)
    

    #close all pop-up-screens
    if not self.edeka_buttons_pressable:    
        if self.close_button.is_clicked(event.pos, not self.edeka_buttons_pressable):

            self.edeka_buttons_pressable = True
            self.movement = True

            self.active_sprites.remove(self.close_button)
            self.active_sprites.remove(self.inventory_screen)
            self.active_sprites.remove(self.settings_screen)
            self.active_sprites.remove(self.deposit_machine)
            self.active_sprites.remove(self.memory_game)
            self.active_sprites.remove(self.space)
            self.active_sprites.remove(self.rendered_cards)
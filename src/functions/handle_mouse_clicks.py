import pygame

from config import *


def handle_mouse_home(self, event):
    if self.settings_button.is_clicked(event.pos, self.home_buttons_pressable):
        self.home_buttons_pressable = False
        self.show_settings = True

    if self.start_button.is_clicked(event.pos, self.home_buttons_pressable):
        pygame.mixer.Sound.play(self.whoosh_sound)
        self.tmp_ticker_start = pygame.time.get_ticks()
        self.black_transition = (True, "walk_into_edeka")
        self.home_buttons_pressable = False
        self.transition_player_info = [int(Iwidth*0.05), -100, Iwidth//15, Iheight//5]

    if self.book.is_clicked(event.pos, self.home_buttons_pressable):
        self.home_buttons_pressable = False
        self.active_sprites.add(self.book_screen)
        self.active_sprites.add(self.close_book)
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
    
    if self.close_book.is_clicked(event.pos, self.show_book):
        self.home_buttons_pressable = True
        self.active_sprites.remove(self.pages[self.book_screen.current_page])
        self.active_sprites.remove(self.book_screen)
        self.active_sprites.remove(self.next_page)
        self.active_sprites.remove(self.last_page)
        self.active_sprites.remove(self.close_book)
        self.show_book = False


def handle_mouse_pre_edeka(self, event):
    return


def handle_mouse_edeka(self, event):
    return
import time

from PIL import ImageDraw

from .helper.displayHelper import *


class Display:
    def __init__(self, color, display_object):
        self.color = color
        self.display_object = display_object
        self.img = setup_img()
        self.draw = ImageDraw.Draw(self.img)
        create_all_static(self.draw, self.color)

    def show_player_selection(self, current_player):
        draw_current_player(self.draw, current_player)
        self.display_object.image(self.img)
        self.display_object.show()
        # self.img.save(f'./png/{time.time()}.png')

    def show_last_roll(self, last_roll):
        self.clear_dice()
        draw_question_mark(self.draw, 95, 35)
        self.display_object.image(self.img)
        self.display_object.show()
        time.sleep(0.5)
        draw_dice_by_cube_eye(self.draw, last_roll)
        self.display_object.image(self.img)
        self.display_object.show()
        # self.img.save(f'./png/{time.time()}.png')

    def show_figure_selection(self, selected_figure):
        draw_figure_selected(self.draw, selected_figure)
        self.display_object.image(self.img)
        self.display_object.show()
        # self.img.save(f'./png/{time.time()}.png')

    def show_player_has_won(self, player_has_won):
        draw_player_won(self.draw, player_has_won)
        self.display_object.image(self.img)
        self.display_object.show()
        # self.img.save(f'./png/{time.time()}.png')

    def show_number_of_players(self, number_of_players):
        draw_players(self.draw, number_of_players)
        self.display_object.image(self.img)
        self.display_object.show()
        # self.img.save(f'./png/{time.time()}.png')

    def show_figure_status(self, figure_index, figure_status):
        draw_figure_status(self.draw, figure_index, figure_status)
        self.display_object.image(self.img)
        self.display_object.show()
        #self.img.save(f'./png/{time.time()}.png')

    def clear_screen(self):
        clearDisplay(self.draw)
        self.display_object.image(self.img)
        self.display_object.show()

    def clear_selected_figure(self):
        clean_figures_selected(self.draw)
        self.display_object.image(self.img)
        self.display_object.show()

    def clear_dice(self):
        clean_dice(self.draw)
        self.display_object.image(self.img)
        self.display_object.show()

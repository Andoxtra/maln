from helper import get_start_field_by_color


class Figure:
    def __init__(self, index_of_figure):
        self.index_of_figure = index_of_figure
        self.position = -1  #-1 => undefined position
        self.able_to_move = False
        self.able_to_beat = False
        self.status = 0  #0 => start, 1 => map, 2 => home
        self.fields_to_go = 39

    def move_figure_on_start_field(self, color_of_player):
        self.position = get_start_field_by_color(color_of_player)
        self.status = 1

    def throw_figure_out(self, b_field):
        self.position = b_field
        self.status = 0
        self.fields_to_go = 39

    def move_figure_forward_on_map(self, last_roll):
        self.position = self.position + last_roll
        self.fields_to_go = self.fields_to_go - last_roll

    def move_figure_around_the_map(self, last_roll):
        self.position = self.position + last_roll - 40
        self.fields_to_go = self.fields_to_go - last_roll

    def move_figure_in_home(self, color_of_player, remainder):
        self.position = color_of_player * 4 + 15 + remainder
        self.status = 2

    def move_figure_forward_in_home(self, last_roll):
        self.position = self.position + last_roll

from helper import *
from .Figure.Figure import Figure
from .IO.Controller import Controller
from .Dice.Dice import Dice

from .config.playerConfig import player_config

from .Phelper.playerHelper import *


def get_last_field_by_color(color):
    return player_config[color]["last_field"]


def create_figures():
    list_of_figures = []
    for x in range(4):
        list_of_figures.append(Figure(x))
    return list_of_figures


def set_player_move_rolled_six_in_home(figure):
    figure.able_to_move = False


def set_player_move_rolled_no_six_in_start(figure):
    figure.able_to_move = False


class Player:
    def __init__(self, color):
        self.color = color
        self.controller = Controller(color, self.get_input_type(), self.get_output_type())
        self.figure_list = create_figures()
        self.last_field = get_last_field_by_color(color)
        self.has_won = False
        self.dice = Dice()

    def roll_the_dice_in_game(self):
        figures_in_home = self.get_figures_by_status(2)
        if len(self.get_figures_by_status(0)) + len(figures_in_home) == 4:
            pos_of_figure_in_home = []
            figures_are_able_to_move_in_home = False
            last_home_field = self.color * 4 + 19
            for figure in figures_in_home:
                pos_of_figure_in_home.append(figure.position)
            for x in range(len(pos_of_figure_in_home)):
                if pos_of_figure_in_home.count(last_home_field - x) == 0:
                    figures_are_able_to_move_in_home = True
            if not figures_are_able_to_move_in_home:
                for index in range(3):
                    self.roll_the_dice()
                    if self.dice.get_rolled_number() == 6:
                        break
            else:
                self.roll_the_dice()

        else:
            self.roll_the_dice()

    def roll_the_dice(self):
        if self.controller.input.wait_for_input_action("Enter"):
            self.dice.roll_dice()
            self.controller.output.show_last_roll(self.dice.get_rolled_number())

    def get_if_figure_can_go_in_home(self, fields_to_go_after_moving):
        if 0 < fields_to_go_after_moving <= 4:
            if not (self.is_own_figure_on_field_by_position(
                    self.color * 4 + 15 + fields_to_go_after_moving)):  # No figure is standing on homeField
                if self.color * 4 + 15 + fields_to_go_after_moving <= self.color * 4 + 19:
                    return True
                else:
                    return False
            else:
                return False
        return False

    def get_able_to_move_when_on_game_field(self, position_of_figure, fields_to_go_figure):
        last_roll = self.dice.get_rolled_number()
        fields_to_go_after_moving = fields_to_go_figure - last_roll
        if position_of_figure + last_roll > 71:
            if fields_to_go_after_moving >= 0:
                if not (self.is_own_figure_on_field_by_position(position_of_figure + last_roll - 40)):
                    return True
                else:
                    return False
            else:
                return self.get_if_figure_can_go_in_home(-fields_to_go_after_moving)
        else:
            if fields_to_go_after_moving >= 0:
                if not (self.is_own_figure_on_field_by_position(position_of_figure + last_roll)):
                    return True
                else:
                    return False
            else:
                return self.get_if_figure_can_go_in_home(-fields_to_go_after_moving)

    def get_possible_moves(self):
        for figure in self.figure_list:
            if self.has_player_rolled_a_six():
                self.player_moves_after_rolled_a_six(figure)
            else:
                self.player_moves_after_rolled_no_six(figure)

    def player_moves_after_rolled_a_six(self, figure):
        if is_figure_in_start(figure):
            self.set_player_move_rolled_six_in_start(figure)
        elif is_figure_in_home(figure):
            set_player_move_rolled_six_in_home(figure)
        elif is_figure_on_gamefield(figure):
            self.set_player_move_rolled_six_on_gamefield(figure)

    def set_player_move_rolled_six_in_start(self, figure):
        if self.is_figure_standing_on_a_field():
            figure.able_to_move = False
        else:
            figure.able_to_move = True

    def is_figure_standing_on_a_field(self):
        start_field = get_start_field_by_color(self.color)
        for figure in self.figure_list:
            if figure.position == start_field:
                return True

    def set_player_move_rolled_six_on_gamefield(self, figure):
        start_field = get_start_field_by_color(self.color)
        if self.get_figures_on_start_field():
            if self.is_figure_standing_on_a_field():
                if figure.position == start_field:
                    if self.is_own_figure_on_field_by_position(start_field + 6):
                        figure.able_to_move = False
                    else:
                        figure.able_to_move = True
                elif figure.position == start_field + 6:
                    figure.able_to_move = True
                else:
                    figure.able_to_move = False
            else:
                figure.able_to_move = False
        else:
            figure.able_to_move = self.get_able_to_move_when_on_game_field(figure.position, figure.fields_to_go)

    def player_moves_after_rolled_no_six(self, figure):
        if is_figure_in_start(figure):
            set_player_move_rolled_no_six_in_start(figure)
        elif is_figure_in_home(figure):
            self.set_player_move_rolled_no_six_in_home(figure)
        elif is_figure_on_gamefield(figure):
            self.set_player_move_rolled_no_six_on_gamefield(figure)

    def set_player_move_rolled_no_six_in_home(self, figure):
        if figure.position + self.dice.get_rolled_number() <= self.color * 4 + 19:
            if not (self.is_own_figure_on_field_by_position(
                    figure.position + self.dice.get_rolled_number())):
                figure.able_to_move = True
            else:
                figure.able_to_move = False
        else:
            figure.able_to_move = False

    def set_player_move_rolled_no_six_on_gamefield(self, figure):
        figure.able_to_move = self.get_able_to_move_when_on_game_field(figure.position, figure.fields_to_go)

    def get_figures_by_status(self, status):
        figures_with_status = []
        for figure in self.figure_list:
            if figure.status == status:
                figures_with_status.append(figure)
        return figures_with_status

    def get_figures_on_start_field(self):
        figures_on_start_field = []
        for figure in self.figure_list:
            if figure.status == 0:
                figures_on_start_field.append(figure)
        return figures_on_start_field

    def get_player_has_won(self):
        figures_in_home = 0
        for figure in self.figure_list:
            if figure.status == 2:
                figures_in_home += 1
        self.has_won = True if figures_in_home == 4 else False
        return self.has_won

    def is_own_figure_on_field_by_position(self, position):
        for figure in self.figure_list:
            if figure.position == position:
                return figure

    def is_figure_able_to_move(self):
        figures_able_to_move = []
        for figure in self.figure_list:
            if figure.able_to_move:
                figures_able_to_move.append(figure)
        return figures_able_to_move

    def has_player_rolled_a_six(self):
        if self.dice.get_rolled_number() == 6:
            return True
        else:
            return False

    def get_input_type(self):
        return player_config[self.color]["input_type"]

    def get_output_type(self):
        return player_config[self.color]["output_type"]

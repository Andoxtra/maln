from .Player.Player import Player
from helper import get_start_field_by_color


def create_full_players():
    list_of_players = []

    for color in range(4):
        list_of_players.append(Player(color))
    return list_of_players


def get_home_list(color_of_player):
    return [color_of_player * 4 + 16 + 0, color_of_player * 4 + 16 + 1, color_of_player * 4 + 16 + 2,
            color_of_player * 4 + 16 + 3]


def get_start_list(color_of_player):
    return [color_of_player * 4 + 0, color_of_player * 4 + 1, color_of_player * 4 + 2, color_of_player * 4 + 3]


def get_b_field_by_fpaf(foreign_player_and_figure):
    foreign_player = foreign_player_and_figure[0]
    foreign_figure = foreign_player_and_figure[1]
    b_field_of_figure = foreign_player.color * 4 + foreign_figure.index_of_figure
    return b_field_of_figure


def get_field_to_land(player, figure):
    last_roll = player.dice.get_rolled_number()
    if figure.status == 0:
        return get_start_field_by_color(player.color)
    elif figure.status == 1:
        field_to_land = figure.position + last_roll
        if field_to_land > 71:
            field_to_land = field_to_land - 40
        if figure.fields_to_go - last_roll < 0:
            field_to_land = player.color * 4 + 15 - (figure.fields_to_go - last_roll)
        return field_to_land
    elif figure.status == 2:
        return figure.position + last_roll


class GameField:
    def __init__(self):
        self.all_players = create_full_players()
        self.standard_play_field = [
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            4, 8, 8, 8, 8, 8, 8, 8, 8, 8,
            5, 8, 8, 8, 8, 8, 8, 8, 8, 8,
            6, 8, 8, 8, 8, 8, 8, 8, 8, 8,
            7, 8, 8, 8, 8, 8, 8, 8, 8, 8,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10
        ]
        self.play_field = self.standard_play_field

    def choose_figure(self, figures_to_choose_from, player):
        index = 0
        length_of_figures_to_choose_from = len(figures_to_choose_from)
        while True:
            self.clean_blinking_field()
            self.change_color_of_selected_figure(figures_to_choose_from, index, player)
            player.controller.output.show_figure_selection(figures_to_choose_from[index].index_of_figure)
            player_input = player.controller.input.get_input()
            if player_input == "Enter":
                return figures_to_choose_from[index]
            elif player_input == "Next":
                index = (index + 1) % length_of_figures_to_choose_from

    def change_color_of_selected_figure(self, list_of_figures, index_of_selected_figure, player):
        for index, figure in enumerate(list_of_figures):
            pos_of_figure = figure.position
            if figure.position == -1:
                pos_of_figure = player.color * 4 + figure.index_of_figure
            if index == index_of_selected_figure:
                self.play_field[pos_of_figure] = player.color
                self.play_field[pos_of_figure + 72] = player.color + 11
                self.play_field[get_field_to_land(player, figure) + 72] = 9
            else:
                self.play_field[pos_of_figure] = player.color

    def get_figure_list_by_color_of_player(self, color_of_player):
        return self.all_players[color_of_player].figure_list

    def clean_blinking_field(self):
        for fieldIndex in range(72, 144):
            self.play_field[fieldIndex] = 10

    def get_current_play_field(self):
        copy_of_play_field_list = self.standard_play_field.copy()
        for player in self.all_players:
            for figure in player.figure_list:
                if figure.position == -1:
                    copy_of_play_field_list[player.color * 4 + figure.index_of_figure] = player.color
                else:
                    copy_of_play_field_list[figure.position] = player.color
        self.play_field = copy_of_play_field_list

    def set_able_to_beat_by_player(self, current_player):
        for own_figure in current_player.figure_list:
            own_figure.able_to_beat = False
        for player in self.all_players:
            if player.color == current_player.color:
                continue
            else:
                for own_figure in current_player.figure_list:
                    for foreignFigure in player.figure_list:
                        if is_own_and_foreign_figure_on_field(own_figure.status, foreignFigure.status):
                            if not own_figure.able_to_beat:
                                end_pos_of_own_figure = get_end_pos_of_own_figure(current_player, own_figure.position)
                                own_figure.able_to_beat = is_foreign_figure_standing_on_end_pos_of_own_figure(
                                    foreignFigure.position, end_pos_of_own_figure)
                            else:
                                break

                        elif is_own_figure_on_start_and_foreign_figure_on_field(
                                own_figure.status, foreignFigure.status):
                            if has_player_rolled_a_six(current_player.dice.get_rolled_number()):
                                if not own_figure.able_to_beat:
                                    end_pos_of_own_figure = get_start_field_by_color(current_player.color)
                                    own_figure.able_to_beat = is_foreign_figure_standing_on_end_pos_of_own_figure(
                                        foreignFigure.position, end_pos_of_own_figure)
                                else:
                                    break
                            else:
                                own_figure.able_to_beat = False

    def get_player_and_figure_by_position(self, position):
        for player in self.all_players:
            for figur in player.figure_list:
                if figur.position == position:
                    return [player, figur]

    def get_figure_by_position_and_throw_out(self, position):
        foreign_player_and_figure = self.get_player_and_figure_by_position(position)
        b_field_of_foreign_figure = get_b_field_by_fpaf(foreign_player_and_figure)
        foreign_player = foreign_player_and_figure[0]
        foreign_figure = foreign_player_and_figure[1]
        foreign_figure.throw_figure_out(b_field_of_foreign_figure)
        foreign_player.controller.output.show_figure_status(foreign_figure.index_of_figure, foreign_figure.status)

    def move_choosen_figure(self, current_player, choosen_figure):
        last_roll = current_player.dice.get_rolled_number()
        position = choosen_figure.position
        color = current_player.color
        start_field = get_start_field_by_color(color)
        place_to_land = position + last_roll
        fields_to_go = choosen_figure.fields_to_go
        if choosen_figure.status == 0:
            if choosen_figure.able_to_beat:
                self.get_figure_by_position_and_throw_out(start_field)
                choosen_figure.move_figure_on_start_field(color)
            else:
                choosen_figure.move_figure_on_start_field(color)

        elif choosen_figure.status == 1:
            if place_to_land > 71 and fields_to_go - last_roll >= 0:
                if choosen_figure.able_to_beat:
                    self.get_figure_by_position_and_throw_out(place_to_land - 40)
                    self.set_old_position_black(position)
                    choosen_figure.move_figure_around_the_map(last_roll)
                else:
                    choosen_figure.move_figure_around_the_map(last_roll)
            elif 0 < last_roll - choosen_figure.fields_to_go <= 4:
                self.set_old_position_black(position)
                choosen_figure.move_figure_in_home(color, last_roll - fields_to_go)
            else:
                if choosen_figure.able_to_beat:
                    self.get_figure_by_position_and_throw_out(place_to_land)
                    self.set_old_position_black(position)
                    choosen_figure.move_figure_forward_on_map(last_roll)
                else:
                    self.set_old_position_black(position)
                    choosen_figure.move_figure_forward_on_map(last_roll)

        elif choosen_figure.status == 2:
            self.set_old_position_black(position)
            choosen_figure.move_figure_forward_in_home(last_roll)

    def set_old_position_black(self, position):
        self.play_field[position] = 10


def get_end_pos_of_own_figure(player, position):
    lastRoll = player.dice.get_rolled_number()
    if is_figure_overstepping_field(position, lastRoll):
        return position + lastRoll - 40
    else:
        return position + lastRoll


def is_own_and_foreign_figure_on_field(own_status, foreign_status):
    if own_status == foreign_status and own_status == 1:
        return True


def is_own_figure_on_start_and_foreign_figure_on_field(own_status, foreign_status):
    if own_status == 0 and foreign_status == 1:
        return True


def is_figure_overstepping_field(figure_position, last_roll=0):
    if figure_position + last_roll > 71:
        return True
    else:
        return False


def is_foreign_figure_standing_on_end_pos_of_own_figure(foreign_figure_position, end_pos_own_figure):
    if foreign_figure_position == end_pos_own_figure:
        return True
    else:
        return False


def has_player_rolled_a_six(last_roll):
    if last_roll == 6:
        return True

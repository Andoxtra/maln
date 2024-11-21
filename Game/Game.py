import time

from .GameField.GameField import GameField

from helper import is_list_empty, get_index_of_highest_number_in_list


def set_is_allowed_to_play(current_player):
    if current_player.dice.get_rolled_number() == 6:
        return True
    else:
        return False


def show_for_all_players_number_of_players(output_of_all_players, number_of_players):
    for single_output in output_of_all_players:
        single_output.show_number_of_players(number_of_players)


def show_for_all_players_player_who_won(output_of_all_players, wining_color):
    for single_output in output_of_all_players:
        single_output.show_player_has_won(wining_color)


def show_for_all_players_figure_on_start(output_of_all_players):
    for single_output in output_of_all_players:
        for index_of_figure in range(4):
            single_output.show_figure_status(index_of_figure, 0)


def show_for_all_players_player_selection(output_of_all_players, current_player):
    for single_output in output_of_all_players:
        single_output.show_player_selection(current_player)


def clear_all_screens(output_of_all_players):
    for single_output in output_of_all_players:
        single_output.clear_screen()


class Game:
    def __init__(self):
        self.game_field = GameField()
        self.play_order = []
        self.running = True

    def game_loop(self):
        self.start_game()

    def get_play_order(self):
        play_order = []
        last_roll_list = []
        amount_of_players = len(self.game_field.all_players)
        output_of_all_players = self.get_output_of_all_players()
        for player in self.game_field.all_players:
            show_for_all_players_player_selection(output_of_all_players, player.color)
            player.roll_the_dice()
            last_roll_list.append(player.dice.get_rolled_number())

        player_with_highest_throw = get_index_of_highest_number_in_list(last_roll_list)
        for x in range(amount_of_players):
            play_order.append((player_with_highest_throw + x) % amount_of_players)
        self.play_order = play_order

    def get_first_player(self):
        return self.game_field.all_players[0]

    def get_all_players(self):
        return self.game_field.all_players

    def get_input_of_first_player(self):
        return self.get_first_player().controller.input

    def get_output_of_all_players(self):
        output_of_all_players = []
        all_players = self.get_all_players()
        for player in all_players:
            output_of_all_players.append(player.controller.output)
        return output_of_all_players

    def get_player_color_who_won(self):
        for player in self.get_all_players():
            if player.has_won:
                return player.color

    def select_number_of_players(self):
        input_of_first_player = self.get_input_of_first_player()
        output_of_all_players = self.get_output_of_all_players()
        number_of_players = 4
        while True:
            show_for_all_players_number_of_players(output_of_all_players, number_of_players)
            player_input = input_of_first_player.get_input()
            if player_input == "Enter":
                self.set_number_of_players(number_of_players)
                break
            elif player_input == "Next":
                number_of_players = 2 if number_of_players == 4 else 4

    def set_number_of_players(self, number_of_players):
        if number_of_players == 2:
            self.game_field.all_players[1].controller.output.clear_screen()
            self.game_field.all_players[3].controller.output.clear_screen()
            self.game_field.all_players.pop(1)
            self.game_field.all_players.pop(2)

    def initialize_game(self):
        print("###############")
        print("get Number of players")
        print("###############")
        self.select_number_of_players()
        print("###############")
        print("Get playorder")
        print("###############")
        self.get_play_order()

    def start_game(self):
        #self.test_leds()
        print("###############")
        print("Start Game")
        print("###############")
        player_has_won = False
        output_of_all_players = self.get_output_of_all_players()
        show_for_all_players_figure_on_start(output_of_all_players)
        self.game_field.get_current_play_field()
        while not player_has_won:
            for player_index in self.play_order:
                is_allowed_to_play = True
                current_player = self.game_field.all_players[player_index]
                show_for_all_players_player_selection(output_of_all_players, current_player.color)
                while is_allowed_to_play:
                    current_player.roll_the_dice_in_game()
                    current_player.get_possible_moves()
                    self.game_field.set_able_to_beat_by_player(current_player)
                    figures_able_to_move = current_player.is_figure_able_to_move()
                    if not is_list_empty(figures_able_to_move):
                        choosen_figure = self.game_field.choose_figure(figures_able_to_move, current_player)
                        self.game_field.move_choosen_figure(current_player, choosen_figure)
                        current_player.controller.output.clear_dice()
                        current_player.controller.output.clear_selected_figure()
                        current_player.controller.output.show_figure_status(
                            choosen_figure.index_of_figure, choosen_figure.status)
                        player_has_won = current_player.get_player_has_won()
                    self.game_field.get_current_play_field()
                    is_allowed_to_play = set_is_allowed_to_play(current_player)
                if player_has_won:
                    break
        color_of_player_who_won = self.get_player_color_who_won()
        show_for_all_players_player_who_won(output_of_all_players, color_of_player_who_won)
        self.winning_animation(color_of_player_who_won)
        clear_all_screens(output_of_all_players)
        self.running = False

    def winning_animation(self, c_p_w):
        playfield_wining_active_template = [
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, 10, c_p_w, 10, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, 10, c_p_w, 10, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, 10, c_p_w, 10, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, 10, c_p_w, 10, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w, c_p_w,
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
        playfield_wining_inactive_template = [
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            c_p_w, c_p_w, c_p_w, c_p_w,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
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
        for x in range(5):
            self.game_field.play_field = playfield_wining_active_template
            time.sleep(1)
            self.game_field.play_field = playfield_wining_inactive_template
            time.sleep(1)

    def test_leds(self):
        testing_map = [
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
        ]
        i = 95
        while True:
            self.game_field.play_field = testing_map
            #print(i)
            #testing_map[i - 1] = 10
            #testing_map[i] = 9
            #i = i + 1
            while True:
                input("")
                break
                #player_input = self.game_field.all_players[0].controller.input.get_input()
                #if player_input == "Enter":
                #    print("Enter")
                #    break

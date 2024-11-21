class Console:
    def __init__(self, color):
        self.color = color

    def show_player_selection(self, current_player):
        print(f"Player Selection  | {self.color} : {current_player}")

    def show_last_roll(self, last_roll):
        print(f"Last Roll         | {self.color} : {last_roll}")

    def show_figure_selection(self, selected_figure):
        print(f"Figure Selection  | {self.color} : {selected_figure}")

    def show_player_has_won(self, player_has_won):
        print(f"Player Has Won    | {self.color} : {player_has_won}")

    def show_number_of_players(self, number_of_players):
        print(f"Number Of Players | {self.color} : {number_of_players}")

    def show_figure_status(self, figure_index, figure_status):
        print(f"Figure {figure_index} | {self.color} : has status {figure_status}")

    def clear_screen(self):
        print(f"Clear Screen  | {self.color}")

    def clear_selected_figure(self):
        print(f"Clear Selected Figure | {self.color}")

    def clear_dice(self):
        print(f"Clear Dice | {self.color}")

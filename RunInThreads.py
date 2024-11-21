import threading
from Game.Game import Game


class RunInThreads:
    def __init__(self, gui_to_run):
        self.game_object = Game()
        self.gui_to_run = gui_to_run

    def start_game_loop(self):
        self.game_object.start_game()

    def get_gui_to_run(self):
        if self.gui_to_run == "Tkinter":
            from GUI.Virtuell.GuiTkinter import GuiTkinter
            return self.initialize_gui(GuiTkinter)
        elif self.gui_to_run == "Physical":
            from GUI.Physical.GuiPhysical import GuiPhysical
            return self.initialize_gui(GuiPhysical)

    def initialize_gui(self, gui):
        return gui(self.game_object)

    def run_game(self):
        self.game_object.initialize_game()
        gui_to_run = self.get_gui_to_run()
        game_thread = threading.Thread(target=self.start_game_loop)
        game_thread.start()
        gui_to_run.render_gui()
        game_thread.join()

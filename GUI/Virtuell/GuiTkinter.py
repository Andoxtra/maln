from tkinter import *
from helper import get_color_code_in_hex


def get_dict_for_game_logi_to_gui():
    dictionary = {
        143: 71,
        142: 70,
        141: 69,
        140: 68,
        139: 67,
        138: 66,
        137: 65,
        136: 64,
        135: 63,
        134: 62,
        133: 61,
        132: 60,
        131: 59,
        130: 58,
        129: 57,
        128: 56,
        127: 55,
        126: 54,
        125: 53,
        124: 52,
        123: 51,
        122: 50,
        121: 49,
        120: 48,
        119: 47,
        118: 46,
        117: 45,
        116: 44,
        115: 43,
        114: 42,
        113: 41,
        112: 40,
        111: 39,
        110: 38,
        109: 37,
        108: 36,
        107: 35,
        106: 34,
        105: 33,
        104: 32,
        103: 31,
        102: 30,
        101: 29,
        100: 28,
        99: 27,
        98: 26,
        97: 25,
        96: 24,
        95: 23,
        94: 22,
        93: 21,
        92: 20,
        91: 19,
        90: 18,
        89: 17,
        88: 16,
        87: 15,
        86: 14,
        85: 13,
        84: 12,
        83: 11,
        82: 10,
        81: 9,
        80: 8,
        79: 7,
        78: 6,
        77: 5,
        76: 4,
        75: 3,
        74: 2,
        73: 1,
        72: 0,
        71: 143,
        70: 142,
        69: 141,
        68: 140,
        67: 139,
        66: 138,
        65: 137,
        64: 136,
        63: 135,
        62: 134,
        61: 133,
        60: 132,
        59: 131,
        58: 130,
        57: 129,
        56: 128,
        55: 127,
        54: 126,
        53: 125,
        52: 124,
        51: 123,
        50: 122,
        49: 121,
        48: 120,
        47: 119,
        46: 118,
        45: 117,
        44: 116,
        43: 115,
        42: 114,
        41: 113,
        40: 112,
        39: 111,
        38: 110,
        37: 109,
        36: 108,
        35: 107,
        34: 106,
        33: 105,
        32: 104,
        31: 103,
        30: 102,
        29: 101,
        28: 100,
        27: 99,
        26: 98,
        25: 97,
        24: 96,
        23: 95,
        22: 94,
        21: 93,
        20: 92,
        19: 91,
        18: 90,
        17: 89,
        16: 88,
        15: 87,
        14: 86,
        13: 85,
        12: 84,
        11: 83,
        10: 82,
        9: 81,
        8: 80,
        7: 79,
        6: 78,
        5: 77,
        4: 76,
        3: 75,
        2: 74,
        1: 73,
        0: 72,
    }
    return dictionary


def map_index_from_game_logic_to_gui(game_logic_index):
    dictionary = get_dict_for_game_logi_to_gui()
    return dictionary[game_logic_index]


class GuiTkinter:
    def __init__(self, game):
        self.game = game
        self.map_config_list = [
            [
                [
                    [40, 40, 80, 80, 10], [120, 40, 160, 80, 10], [40, 120, 80, 160, 10], [120, 120, 160, 160, 10],
                    [760, 40, 800, 80, 10], [840, 40, 880, 80, 10], [760, 120, 800, 160, 10], [840, 120, 880, 160, 10],
                    [760, 760, 800, 800, 10], [840, 760, 880, 800, 10], [760, 840, 800, 880, 10],
                    [840, 840, 880, 880, 10],
                    [40, 760, 80, 800, 10], [120, 760, 160, 800, 10], [40, 840, 80, 880, 10], [120, 840, 160, 880, 10],

                    [120, 440, 160, 480, 10], [200, 440, 240, 480, 10], [280, 440, 320, 480, 10],
                    [360, 440, 400, 480, 10],
                    [440, 120, 480, 160, 10], [440, 200, 480, 240, 10], [440, 280, 480, 320, 10],
                    [440, 360, 480, 400, 10],
                    [760, 440, 800, 480, 10], [680, 440, 720, 480, 10], [600, 440, 640, 480, 10],
                    [520, 440, 560, 480, 10],
                    [440, 760, 480, 800, 10], [440, 680, 480, 720, 10], [440, 600, 480, 640, 10],
                    [440, 520, 480, 560, 10],

                    [40, 360, 80, 400, 10],
                    [120, 360, 160, 400, 10],
                    [200, 360, 240, 400, 10],
                    [280, 360, 320, 400, 10],
                    [360, 360, 400, 400, 10],
                    [360, 280, 400, 320, 10],
                    [360, 200, 400, 240, 10],
                    [360, 120, 400, 160, 10],
                    [360, 40, 400, 80, 10],
                    [440, 40, 480, 80, 10],
                    [520, 40, 560, 80, 10],
                    [520, 120, 560, 160, 10],
                    [520, 200, 560, 240, 10],
                    [520, 280, 560, 320, 10],
                    [520, 360, 560, 400, 10],
                    [600, 360, 640, 400, 10],
                    [680, 360, 720, 400, 10],
                    [760, 360, 800, 400, 10],
                    [840, 360, 880, 400, 10],
                    [840, 440, 880, 480, 10],
                    [840, 520, 880, 560, 10],
                    [760, 520, 800, 560, 10],
                    [680, 520, 720, 560, 10],
                    [600, 520, 640, 560, 10],
                    [520, 520, 560, 560, 10],
                    [520, 600, 560, 640, 10],
                    [520, 680, 560, 720, 10],
                    [520, 760, 560, 800, 10],
                    [520, 840, 560, 880, 10],
                    [440, 840, 480, 880, 10],
                    [360, 840, 400, 880, 10],
                    [360, 760, 400, 800, 10],
                    [360, 680, 400, 720, 10],
                    [360, 600, 400, 640, 10],
                    [360, 520, 400, 560, 10],
                    [280, 520, 320, 560, 10],
                    [200, 520, 240, 560, 10],
                    [120, 520, 160, 560, 10],
                    [40, 520, 80, 560, 10],
                    [40, 440, 80, 480, 10]
                ], 1
            ],
            [
                [
                    [40, 40, 80, 80, 0], [120, 40, 160, 80, 0], [40, 120, 80, 160, 0], [120, 120, 160, 160, 0],
                    [760, 40, 800, 80, 1], [840, 40, 880, 80, 1], [760, 120, 800, 160, 1], [840, 120, 880, 160, 1],
                    [760, 760, 800, 800, 2], [840, 760, 880, 800, 2], [760, 840, 800, 880, 2], [840, 840, 880, 880, 2],
                    [40, 760, 80, 800, 3], [120, 760, 160, 800, 3], [40, 840, 80, 880, 3], [120, 840, 160, 880, 3],

                    [120, 440, 160, 480, 0], [200, 440, 240, 480, 0], [280, 440, 320, 480, 0], [360, 440, 400, 480, 0],
                    [440, 120, 480, 160, 1], [440, 200, 480, 240, 1], [440, 280, 480, 320, 1], [440, 360, 480, 400, 1],
                    [760, 440, 800, 480, 2], [680, 440, 720, 480, 2], [600, 440, 640, 480, 2], [520, 440, 560, 480, 2],
                    [440, 760, 480, 800, 3], [440, 680, 480, 720, 3], [440, 600, 480, 640, 3], [440, 520, 480, 560, 3],

                    [40, 360, 80, 400, 0],
                    [120, 360, 160, 400, 4],
                    [200, 360, 240, 400, 4],
                    [280, 360, 320, 400, 4],
                    [360, 360, 400, 400, 4],
                    [360, 280, 400, 320, 4],
                    [360, 200, 400, 240, 4],
                    [360, 120, 400, 160, 4],
                    [360, 40, 400, 80, 4],
                    [440, 40, 480, 80, 4],
                    [520, 40, 560, 80, 1],
                    [520, 120, 560, 160, 4],
                    [520, 200, 560, 240, 4],
                    [520, 280, 560, 320, 4],
                    [520, 360, 560, 400, 4],
                    [600, 360, 640, 400, 4],
                    [680, 360, 720, 400, 4],
                    [760, 360, 800, 400, 4],
                    [840, 360, 880, 400, 4],
                    [840, 440, 880, 480, 4],
                    [840, 520, 880, 560, 2],
                    [760, 520, 800, 560, 4],
                    [680, 520, 720, 560, 4],
                    [600, 520, 640, 560, 4],
                    [520, 520, 560, 560, 4],
                    [520, 600, 560, 640, 4],
                    [520, 680, 560, 720, 4],
                    [520, 760, 560, 800, 4],
                    [520, 840, 560, 880, 4],
                    [440, 840, 480, 880, 4],
                    [360, 840, 400, 880, 3],
                    [360, 760, 400, 800, 4],
                    [360, 680, 400, 720, 4],
                    [360, 600, 400, 640, 4],
                    [360, 520, 400, 560, 4],
                    [280, 520, 320, 560, 4],
                    [200, 520, 240, 560, 4],
                    [120, 520, 160, 560, 4],
                    [40, 520, 80, 560, 4],
                    [40, 440, 80, 480, 4]
                ], 0
            ]
        ]
        self.config_elements = []
        self.root = Tk()
        self.canvas = Canvas(self.root, height=920, width=920, bg="white")
        self.update_interval = 300

    def reload_playing_field(self):
        for index, color in enumerate(self.game.game_field.play_field):
            element = self.config_elements[map_index_from_game_logic_to_gui(index)]
            if color >= 11:
                self.blink_color_of_field(element, get_color_code_in_hex(color))
            else:
                self.change_color_of_field(element, get_color_code_in_hex(color))

    def change_color_of_field(self, element, color):
        self.canvas.itemconfig(element, fill=color)

    def blink_color_of_field(self, element, color):
        current_color = self.canvas.itemcget(element, "fill")
        if current_color == "#000000":
            self.change_color_of_field(element, color)
        else:
            self.change_color_of_field(element, "#000000")

    def append_config_elements_oval(self, list_of_config_elements):
        for index, config_element in enumerate(list_of_config_elements):
            color_in_hex = get_color_code_in_hex(config_element[4])
            self.config_elements.append(
                self.canvas.create_oval(config_element[0], config_element[1], config_element[2], config_element[3],
                                        fill=color_in_hex, outline="black", width=1))
            self.canvas.create_text(config_element[0]-10, config_element[1]-10, text=index)

    def append_config_elements_rectangle(self, list_of_config_elements):
        for config_element in list_of_config_elements:
            color_in_hex = get_color_code_in_hex(config_element[4])
            self.config_elements.append(
                self.canvas.create_rectangle(config_element[0], config_element[1], config_element[2], config_element[3],
                                             fill=color_in_hex))

    def set_config_elements(self):
        for list_item in self.map_config_list:
            shape = list_item[1]
            if shape == 0:
                self.append_config_elements_oval(list_item[0])
            elif shape == 1:
                self.append_config_elements_rectangle(list_item[0])

    def render_gui(self):
        self.root.title("Mensch Ärgere Licht Nicht")
        self.root.geometry("920x920")
        self.canvas.pack()
        self.set_config_elements()
        self.update_gui()
        self.root.mainloop()

    def update_gui(self):
        self.reload_playing_field()
        if not self.game.running:
            self.root.after(0, self.root.destroy)
        self.root.after(self.update_interval, self.update_gui)

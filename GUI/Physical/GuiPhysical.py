import board
import neopixel_spi as neopixel
import time

from helper import get_color_code_in_int


def get_index_from_map(index):
    map = {
        0: 7, 1: 9, 2: 5, 3: 11,
        4: 41, 5: 43, 6: 47, 7: 45,
        8: 83, 9: 77, 10: 81, 11: 79,
        12: 117, 13: 119, 14: 115, 15: 113,

        16: 15, 17: 17, 18: 23, 19: 25,
        20: 51, 21: 53, 22: 59, 23: 61,
        24: 87, 25: 89, 26: 95, 27: 97,
        28: 123, 29: 125, 30: 131, 31: 133,

        32: 3, 33: 13, 34: 19, 35: 21, 36: 27, 37: 29, 38: 31, 39: 33, 40: 35, 41: 37,
        42: 39, 43: 49, 44: 55, 45: 57, 46: 63, 47: 65, 48: 67, 49: 69, 50: 71, 51: 73,
        52: 75, 53: 85, 54: 91, 55: 93, 56: 99, 57: 101, 58: 103, 59: 105, 60: 107, 61: 109,
        62: 111, 63: 121, 64: 127, 65: 129, 66: 135, 67: 137, 68: 139, 69: 141, 70: 143, 71: 1,

        72: 6, 73: 8, 74: 4, 75: 10,
        76: 40, 77: 42, 78: 46, 79: 44,
        80: 82, 81: 76, 82: 80, 83: 78,
        84: 116, 85: 118, 86: 114, 87: 112,

        88: 14, 89: 16, 90: 22, 91: 24,
        92: 50, 93: 52, 94: 58, 95: 60,
        96: 86, 97: 88, 98: 94, 99: 96,
        100: 122, 101: 124, 102: 130, 103: 132,

        104: 2, 105: 12, 106: 18, 107: 20, 108: 26, 109: 28, 110: 30, 111: 32, 112: 34, 113: 36,
        114: 38, 115: 48, 116: 54, 117: 56, 118: 62, 119: 64, 120: 66, 121: 68, 122: 70, 123: 72,
        124: 74, 125: 84, 126: 90, 127: 92, 128: 98, 129: 100, 130: 102, 131: 104, 132: 106, 133: 108,
        134: 110, 135: 120, 136: 126, 137: 128, 138: 134, 139: 136, 140: 138, 141: 140, 142: 142, 143: 0,
    }
    return map[index]


class GuiPhysical:
    def __init__(self, game):
        numOfPixel = 144
        pixel_order = neopixel.GRB
        spi = board.SPI()
        brightness_of_le_ds = 1
        self.pixels = neopixel.NeoPixel_SPI(spi, numOfPixel, pixel_order=pixel_order, auto_write=True, bit0=0b10000000,
                                            brightness=brightness_of_le_ds)
        self.update_interval = 0.3
        self.game = game

    def reload_leds(self):
        for index, color in enumerate(self.game.game_field.play_field):
            color_in_int = get_color_code_in_int(color)
            if color >= 11:
                self.blink_led_by_index_and_color(index, color_in_int)
            else:
                self.set_color_of_led_by_index(index, color_in_int)

    def blink_led_by_index_and_color(self, index, color_int):
        newIndex = get_index_from_map(index)
        current_color = self.pixels[newIndex]
        if current_color == [0, 0, 0]:
            self.set_color_of_led_by_index(index, color_int)
        else:
            self.set_color_of_led_by_index(index, (0, 0, 0))

    def update_leds(self):
        while self.game.running:
            self.reload_leds()
            time.sleep(self.update_interval)

    def render_gui(self):
        self.update_leds()

    def set_color_of_led_by_index(self, index, color):
        newIndex = get_index_from_map(index)
        self.pixels[newIndex] = color

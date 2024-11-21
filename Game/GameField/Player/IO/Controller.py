import busio

from .Input.Physical.PortExpander import PortExpander
from .Input.Virtuell.Keyboard import Keyboard
from .Output.Virtuell.Console import Console
from .Output.Physical.Display import Display

from .config.physicalAddressConfig import physical_address_config


def get_i2_c_bus_pins_by_color(color):
    return physical_address_config[color]["i2c"]


def get_display_address_by_color(color):
    return physical_address_config[color]["display"]


def get_port_expander_address_by_color(color) -> int:
    return physical_address_config[color]["portExpander"]


class Controller:
    def __init__(self, color, input_type, output_type):
        self.color = color
        self.input = None
        self.output = None
        self.pins_in_dic = None
        self.i2c_bus_object = None
        self.input_type = input_type
        self.output_type = output_type

        self.get_input()
        self.get_output()

    def get_input(self):
        if self.input_type == "Physical":
            import board
            pins_in_dic = get_i2_c_bus_pins_by_color(self.color)
            self.i2c_bus_object = busio.I2C(getattr(board, pins_in_dic["SCL"]), getattr(board, pins_in_dic["SDA"]))
            self.input = PortExpander(self.i2c_bus_object, get_port_expander_address_by_color(self.color))

        elif self.input_type == "Keyboard":
            self.input = Keyboard()

    def get_output(self):
        if self.output_type == "LCDDisplay":
            import adafruit_ssd1306
            import board
            pinsInDic = get_i2_c_bus_pins_by_color(self.color)
            self.pins_in_dic = busio.I2C(getattr(board, pinsInDic["SCL"]), getattr(board, pinsInDic["SDA"]))
            self.i2c_bus_object = adafruit_ssd1306.SSD1306_I2C(
                128, 64, self.pins_in_dic, addr=get_display_address_by_color(self.color))
            self.output = Display(self.color, self.i2c_bus_object)

        elif self.output_type == "Console":
            self.output = Console(self.color)

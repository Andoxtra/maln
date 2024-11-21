from adafruit_mcp230xx.mcp23008 import MCP23008
from .PhysicalButton import PhysicalButton


class PortExpander:
    def __init__(self, i2c_bus_object, address_of_port_expander):
        self.expander = MCP23008(i2c_bus_object, address=address_of_port_expander)
        self.next_button = PhysicalButton(self.expander, 1, "Next")
        self.enter_button = PhysicalButton(self.expander, 0, "Enter")
        self.list_of_buttons = [self.next_button, self.enter_button]

    def get_input(self):
        return self.is_one_button_pressed_and_released()

    def wait_for_input_action(self, input_action):
        while True:
            return_message = self.get_input()
            if return_message == input_action:
                return True

    def is_one_button_pressed_and_released(self):
        while True:
            for button in self.list_of_buttons:
                if button.is_button_pressed():
                    while True:
                        if button.is_button_released():
                            return button.return_message

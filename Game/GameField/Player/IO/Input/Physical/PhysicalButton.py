from digitalio import Pull, Direction


class PhysicalButton:
    def __init__(self, expander, pin, return_message):
        self.pin = pin
        self.return_message = return_message
        self.expander = expander
        self.pin_to_read = expander.get_pin(pin)
        self.setup_pin_to_read()

    def setup_pin_to_read(self):
        self.pin_to_read.direction = Direction.INPUT
        self.pin_to_read.pull = Pull.UP

    def is_button_pressed(self):
        if not self.pin_to_read.value:
            return self.return_message

    def is_button_released(self):
        if self.pin_to_read.value:
            return True

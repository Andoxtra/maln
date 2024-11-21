import keyboard


class Keyboard:
    def __init__(self):
        self.valid_dict_map_keys = get_valid_dict_map_keys()
        self.key_press = ""

    def get_key_press(self):
        key_event = keyboard.read_event()
        if key_event.event_type == "down":
            self.key_press = key_event.name

    def is_key_press_in_valid_keys(self):
        self.get_key_press()
        validKeys = self.getKeysOfDict()
        if self.key_press in validKeys:
            return True
        return False

    def map_key_press(self):
        return self.valid_dict_map_keys[self.key_press]

    def getKeysOfDict(self):
        map_of_keys = self.valid_dict_map_keys
        return map_of_keys.keys()

    def is_keyboard_button_pressed(self):
        while True:
            self.get_key_press()
            if self.is_key_press_in_valid_keys():
                return self.map_key_press()

    def get_input(self):
        return self.is_keyboard_button_pressed()

    def wait_for_input_action(self, input_action):
        while True:
            player_input = self.get_input()
            if player_input == input_action:
                return True


def get_valid_dict_map_keys():
    valid_dict_map_keys = {
        "d": "Next",
        "enter": "Enter"
    }
    return valid_dict_map_keys

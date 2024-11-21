import random


class Dice:
    def __init__(self):
        self.rolled_number = None
        self.range_from = 1
        self.range_to = 6

    def roll_dice(self):
        self.rolled_number = random.randint(self.range_from, self.range_to)

    def get_rolled_number(self):
        return self.rolled_number

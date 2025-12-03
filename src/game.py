# The Game class handles the logic for a single Monty Hall game.
# It manages the three doors, prize placement, player choices, and host actions.

from random import randint
from door import Door


class Game:
    # Initialize the game with three doors
    def __init__(self):
        self.doors = [Door(0), Door(1), Door(2)]
        self.prize_door = None
        self.player_initial_choice = None
        self.host_opened_door = None

    # Randomly place the prize behind one of the three doors
    def setup_game(self):
        self.prize_door = randint(0, 2)
        self.doors[self.prize_door].place_prize()

    # Player randomly selects one door as their initial choice
    def player_choose(self):
        self.player_initial_choice = randint(0, 2)
        return self.player_initial_choice

    # Host opens a door that is not the player's choice and does not have the prize
    def host_open_door(self):
        for i in range(3):
            if i != self.player_initial_choice and not self.doors[i].has_prize():
                self.host_opened_door = i
                return self.host_opened_door
        return None

    # Get the door number that the player would switch to
    def get_switch_door(self):
        for i in range(3):
            if i != self.player_initial_choice and i != self.host_opened_door:
                return i
        return None

    # Play the game with the stay strategy and return True if player wins
    def play_stay(self):
        return self.doors[self.player_initial_choice].has_prize()

    # Play the game with the switch strategy and return True if player wins
    def play_switch(self):
        switch_door = self.get_switch_door()
        return self.doors[switch_door].has_prize()

    # Return string representation of the current game state
    def __str__(self):
        return (f"Prize: Door {self.prize_door}, "
                f"Player chose: Door {self.player_initial_choice}, "
                f"Host opened: Door {self.host_opened_door}")

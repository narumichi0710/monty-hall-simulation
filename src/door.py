# The Door class represents a single door in the Monty Hall game.
# Each door can either have a prize behind it or not.

class Door:
    # Initialize a door with a given number and no prize
    def __init__(self, door_number):
        self.door_number = door_number
        self._has_prize = False

    # Place the prize behind this door
    def place_prize(self):
        self._has_prize = True

    # Check if this door has the prize
    def has_prize(self):
        return self._has_prize

    # Return string representation of the door
    def __str__(self):
        return f"Door {self.door_number}"

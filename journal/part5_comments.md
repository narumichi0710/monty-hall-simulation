# PART 5: Commenting Your Program

This section contains the full program code with thorough comments explaining each part.

---

## The door.py file

```python
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
```

---

## The game.py file

```python
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
```

---

## The main.py file

```python
# Monty Hall Simulation
# This program simulates the Monty Hall problem to demonstrate
# that switching doors gives a higher probability of winning (2/3)
# compared to staying with the initial choice (1/3).

from game import Game
from datetime import datetime


# Play one sample game and display each step to the user
def play_sample_game():
    print("=" * 50)
    print("Running one sample game to demonstrate the rules:")
    print("=" * 50)

    # Create a new game instance
    game = Game()
    game.setup_game()

    # Player makes initial choice
    initial_choice = game.player_choose()
    print(f"Player initially chose: Door {initial_choice}")

    # Host opens a door with a goat
    host_opened = game.host_open_door()
    print(f"Host opens: Door {host_opened} (revealing a goat)")

    # Show which door the player would switch to
    switch_door = game.get_switch_door()
    print(f"If player switches, they would choose: Door {switch_door}")

    print()
    # Show results for both strategies
    if game.play_stay():
        print("Result if player STAYS: WIN!")
    else:
        print("Result if player STAYS: LOSE")

    if game.play_switch():
        print("Result if player SWITCHES: WIN!")
    else:
        print("Result if player SWITCHES: LOSE")

    # Reveal where the prize was
    print(f"\n(Prize was behind: Door {game.prize_door})")
    print("=" * 50)
    print()


# Run multiple simulations and track results for both strategies
def run_simulation(number_of_games):
    # Initialize win counters
    stay_wins = 0
    switch_wins = 0

    # Run the simulation for the specified number of games
    for _ in range(number_of_games):
        game = Game()
        game.setup_game()
        game.player_choose()
        game.host_open_door()

        # Check if stay strategy wins
        if game.play_stay():
            stay_wins += 1

        # Check if switch strategy wins
        if game.play_switch():
            switch_wins += 1

    # Calculate percentages
    stay_percentage = (stay_wins / number_of_games) * 100
    switch_percentage = (switch_wins / number_of_games) * 100

    # Display results to the user
    print()
    print("=" * 50)
    print("SIMULATION RESULTS")
    print("=" * 50)
    print(f"Total games played: {number_of_games}")
    print()
    print(f"STAY strategy:   {stay_wins} wins ({stay_percentage:.2f}%)")
    print(f"SWITCH strategy: {switch_wins} wins ({switch_percentage:.2f}%)")
    print("=" * 50)

    # Log results to file for record-keeping
    log_results(stay_wins, switch_wins, number_of_games)
    print("Results have been saved to log.txt")


# Save simulation results to a log file
def log_results(stay_wins, switch_wins, number_of_games):
    # Calculate percentages for logging
    stay_percentage = (stay_wins / number_of_games) * 100
    switch_percentage = (switch_wins / number_of_games) * 100

    # Open file in append mode to preserve previous results
    with open("log.txt", "a") as file:
        # Get current date and time for the log entry
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

        # Write the simulation results to the file
        file.write(f"\n{'=' * 40}\n")
        file.write(f"Date and time: {dt_string}\n")
        file.write(f"Total games: {number_of_games}\n")
        file.write(f"Stay wins: {stay_wins} ({stay_percentage:.2f}%)\n")
        file.write(f"Switch wins: {switch_wins} ({switch_percentage:.2f}%)\n")


# Main function - entry point of the program
def main():
    print()
    print("Welcome to the Monty Hall Simulation!")
    print()

    # Show a sample game first to demonstrate how the game works
    play_sample_game()

    number = 0

    # Keep asking until a valid positive number is entered
    # This loop ensures the user provides valid input
    while number <= 0:
        user_input = input("How many games would you like to simulate? ")

        # Try to convert input to integer, handle invalid input
        try:
            number = int(user_input)

            # Check if the number is positive
            if number <= 0:
                print("Please enter a positive number.")
                number = 0
            else:
                # Run the simulation with the valid number
                run_simulation(number)
        except ValueError:
            # Handle non-numeric input
            print("Please enter a valid number.")


# Standard Python idiom to run main() when script is executed directly
if __name__ == "__main__":
    main()
```

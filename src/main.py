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

    game = Game()
    game.setup_game()

    initial_choice = game.player_choose()
    print(f"Player initially chose: Door {initial_choice}")

    host_opened = game.host_open_door()
    print(f"Host opens: Door {host_opened} (revealing a goat)")

    switch_door = game.get_switch_door()
    print(f"If player switches, they would choose: Door {switch_door}")

    print()
    if game.play_stay():
        print("Result if player STAYS: WIN!")
    else:
        print("Result if player STAYS: LOSE")

    if game.play_switch():
        print("Result if player SWITCHES: WIN!")
    else:
        print("Result if player SWITCHES: LOSE")

    print(f"\n(Prize was behind: Door {game.prize_door})")
    print("=" * 50)
    print()


# Run multiple simulations and track results for both strategies
def run_simulation(number_of_games):
    stay_wins = 0
    switch_wins = 0

    # Run the simulation for the specified number of games
    for _ in range(number_of_games):
        game = Game()
        game.setup_game()
        game.player_choose()
        game.host_open_door()

        if game.play_stay():
            stay_wins += 1

        if game.play_switch():
            switch_wins += 1

    # Calculate percentages
    stay_percentage = (stay_wins / number_of_games) * 100
    switch_percentage = (switch_wins / number_of_games) * 100

    # Display results
    print()
    print("=" * 50)
    print("SIMULATION RESULTS")
    print("=" * 50)
    print(f"Total games played: {number_of_games}")
    print()
    print(f"STAY strategy:   {stay_wins} wins ({stay_percentage:.2f}%)")
    print(f"SWITCH strategy: {switch_wins} wins ({switch_percentage:.2f}%)")
    print("=" * 50)

    # Log results to file
    log_results(stay_wins, switch_wins, number_of_games)
    print("Results have been saved to log.txt")


# Save simulation results to a log file
def log_results(stay_wins, switch_wins, number_of_games):
    stay_percentage = (stay_wins / number_of_games) * 100
    switch_percentage = (switch_wins / number_of_games) * 100

    with open("log.txt", "a") as file:
        # Get current date and time
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

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

    # Show a sample game first
    play_sample_game()

    number = 0

    # Keep asking until a valid positive number is entered
    while number <= 0:
        user_input = input("How many games would you like to simulate? ")

        try:
            number = int(user_input)

            if number <= 0:
                print("Please enter a positive number.")
                number = 0
            else:
                run_simulation(number)
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()

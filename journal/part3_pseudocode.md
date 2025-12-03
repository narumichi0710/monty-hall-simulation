# PART 3: Generalizing Into Pseudocode

## Class Door

```
Class Door
    Initialize with door_number
        Set door_number to the given number
        Set has_prize to False

    Method place_prize()
        Set has_prize to True

    Method has_prize()
        Return has_prize value
```

## Class Game

```
Class Game
    Initialize
        Create three Door objects (door 0, door 1, door 2)
        Set prize_door to None
        Set player_initial_choice to None
        Set host_opened_door to None

    Method setup_game()
        Randomly select one door (0, 1, or 2) for the prize
        Place the prize behind that door
        Set prize_door to the selected door number

    Method player_choose()
        Randomly select one door (0, 1, or 2) as initial choice
        Set player_initial_choice to the selected door number
        Return player_initial_choice

    Method host_open_door()
        For each door in doors
            If door is not player_initial_choice AND door does not have prize
                Set host_opened_door to that door number
                Return host_opened_door

    Method get_switch_door()
        For each door in doors
            If door is not player_initial_choice AND door is not host_opened_door
                Return that door number

    Method play_stay()
        Return True if door at player_initial_choice has prize, else False

    Method play_switch()
        Get the switch_door using get_switch_door()
        Return True if door at switch_door has prize, else False
```

## Main Program

```
Function play_sample_game()
    Create a new Game
    Call setup_game()
    Call player_choose() and display the choice
    Call host_open_door() and display which door was opened
    Display what happens if player stays
    Display what happens if player switches

Function run_simulation(number_of_games)
    Set stay_wins to 0
    Set switch_wins to 0

    Loop from 1 to number_of_games
        Create a new Game
        Call setup_game()
        Call player_choose()
        Call host_open_door()

        If play_stay() returns True
            Add 1 to stay_wins

        If play_switch() returns True
            Add 1 to switch_wins

    Calculate stay_percentage as stay_wins / number_of_games * 100
    Calculate switch_percentage as switch_wins / number_of_games * 100

    Display total stay wins and percentage
    Display total switch wins and percentage

    Call log_results(stay_wins, switch_wins, number_of_games)

Function log_results(stay_wins, switch_wins, number_of_games)
    Open log file in append mode
    Write current date and time
    Write stay wins and percentage
    Write switch wins and percentage
    Close file

Main
    Display welcome message
    Call play_sample_game()

    Set number to 0

    Loop while number is less than or equal to 0
        Prompt user for number of simulations
        Try to convert input to integer
            If input is less than or equal to 0
                Display error message
                Set number to 0
            Else
                Call run_simulation(number)
        If ValueError occurs
            Display error message asking for a valid number
```

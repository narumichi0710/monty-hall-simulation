# PART 1: Defining Your Problem

## Problem Description

The Monty Hall problem is a famous probability puzzle that demonstrates how counterintuitive probability can be. The problem is named after Monty Hall, the host of the TV game show "Let's Make a Deal."

The goal of this program is to simulate the Monty Hall problem and statistically verify which strategy is mathematically advantageous: "switching doors" or "staying with the initial choice."

## Input Data

- The user will input the number of simulations to run (a positive integer).
- The program will validate the input to ensure it is a valid positive number.

## Program Functionality

The program will:

1. Display a sample game to show the user how the Monty Hall game works.
2. Ask the user to input the number of simulations to run.
3. For each simulation:
   - Randomly place the prize behind one of three doors.
   - Randomly select an initial door for the player.
   - The host opens one of the remaining doors that does not contain the prize.
   - Track the outcome for both strategies (switch and stay).
4. Calculate and display statistics after all simulations are complete.

## Expected Outputs

The program will output:

- Total number of wins for the "switch" strategy.
- Total number of wins for the "stay" strategy.
- Winning percentage for each strategy.
- The results will also be saved to an external log file for record-keeping.

By running many simulations, users will see that switching doors results in approximately 66.7% wins, while staying results in approximately 33.3% wins.

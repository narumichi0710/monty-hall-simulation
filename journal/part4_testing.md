# PART 4: Testing Your Program

## Test Case 1: Valid Input

**Test:** Enter a valid positive number (1000) for the number of simulations.

**Purpose:** Verify that the program correctly runs the simulation and displays accurate statistics.

**Result:** The program successfully ran 1000 simulations and displayed:
- Stay wins: approximately 33-34%
- Switch wins: approximately 65-67%

This matches the theoretical probability (1/3 for stay, 2/3 for switch), confirming the simulation logic is correct.

## Test Case 2: Invalid Input - Non-numeric

**Test:** Enter a letter "a" instead of a number.

**Initial Code Issue:** The program would crash with a `ValueError` if the user entered non-numeric input.

**Error Observed:**
```
ValueError: invalid literal for int() with base 10: 'a'
```

**Fix Applied:** Added try-except block to catch `ValueError`:

```python
try:
    number = int(user_input)
    # ... rest of logic
except ValueError:
    print("Please enter a valid number.")
```

**Result After Fix:** The program now displays "Please enter a valid number." and prompts the user again.

## Test Case 3: Invalid Input - Zero or Negative Number

**Test:** Enter "0" or "-5" for the number of simulations.

**Initial Code Issue:** The program accepted 0 or negative numbers, which caused incorrect results or division by zero errors.

**Fix Applied:** Added validation to check if the number is greater than 0:

```python
if number <= 0:
    print("Please enter a positive number.")
    number = 0
else:
    run_simulation(number)
```

**Result After Fix:** The program now displays "Please enter a positive number." and prompts the user again.

## Test Case 4: While Loop for Continuous Input

**Test:** Enter multiple invalid inputs in a row ("a", then "-1", then "0").

**Initial Code Issue:** Similar to the craps example in the sample journal, the program would stop after handling the exception instead of asking for input again.

**Fix Applied:** Wrapped the input logic in a `while number <= 0:` loop:

```python
number = 0
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
```

**Result After Fix:** The program continues to prompt the user until a valid positive number is entered.

## Test Case 5: Edge Case - Single Simulation

**Test:** Enter "1" to run only one simulation.

**Purpose:** Verify the program handles the minimum valid input correctly.

**Result:** The program correctly runs one game and displays results (either 0% or 100% for each strategy, since only one game was played).

## Test Case 6: Large Number of Simulations

**Test:** Enter "100000" to run a large number of simulations.

**Purpose:** Verify the program can handle large numbers and that results converge to theoretical values.

**Result:** With 100,000 simulations:
- Stay wins: approximately 33.3%
- Switch wins: approximately 66.7%

The results closely match the theoretical probability, confirming the simulation's accuracy.

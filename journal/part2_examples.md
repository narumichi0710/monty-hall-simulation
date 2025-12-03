# PART 2: Working Through Specific Examples

## Scenario 1: Player stays and loses

**Initial Setup:** Prize is behind Door A.

1. The prize is randomly placed behind Door A.
2. The player randomly selects Door B as their initial choice.
3. The host opens Door C, revealing a goat (no prize).
4. The player decides to stay with Door B.
5. The player opens Door B and finds a goat.
6. **Result: Player loses.**

## Scenario 2: Player stays and wins

**Initial Setup:** Prize is behind Door B.

1. The prize is randomly placed behind Door B.
2. The player randomly selects Door B as their initial choice.
3. The host opens Door A or Door C, revealing a goat.
4. The player decides to stay with Door B.
5. The player opens Door B and finds the prize.
6. **Result: Player wins.**

## Scenario 3: Player switches and wins

**Initial Setup:** Prize is behind Door A.

1. The prize is randomly placed behind Door A.
2. The player randomly selects Door B as their initial choice.
3. The host opens Door C, revealing a goat (the host cannot open Door A because it has the prize, and cannot open Door B because the player selected it).
4. The player decides to switch from Door B to Door A.
5. The player opens Door A and finds the prize.
6. **Result: Player wins.**

## Scenario 4: Player switches and loses

**Initial Setup:** Prize is behind Door C.

1. The prize is randomly placed behind Door C.
2. The player randomly selects Door C as their initial choice.
3. The host opens Door A or Door B, revealing a goat.
4. The player decides to switch from Door C to the remaining unopened door.
5. The player opens the switched door and finds a goat.
6. **Result: Player loses.**

## Key Observations

- When the player **stays**: They win only if their initial choice was correct (1/3 probability).
- When the player **switches**: They win if their initial choice was wrong (2/3 probability).
- The host's action of revealing a goat provides information that changes the probability distribution.

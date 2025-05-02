# Mastermind (Python)

## Project Description

This program is a command-line Python implementation of the classic board game **Mastermind**, developed for a class assignment. It features you as the human player (the **codebreaker**) going up against the computer (the **codemaker**).

The computer randomly selects a hidden sequence of four colored pegs. You have **10 attempts** to guess the correct sequence. After each guess, the program provides helpful clues to guide your next attempt.


## Running the Program

To run the program from the terminal, use:

```
py mastermind.py
```
Alternatively, use `python` instead of `py` if that is how your system invokes Python 3.


## How to Play

When the program starts, you will be prompted to enter a random seed:
  - Enter any integer for a repeatable code sequence (useful for testing or retrying a known code).
  - Press Enter without typing a number to generate a completely random code.

Each round, you will guess four colors by entering four numbers, one at a time.

Valid color inputs:
  - 0 - red
  - 1 - orange
  - 2 - yellow
  - 3 - green
  - 4 - blue
  - 5 - purple

After each full guess, the program gives you a clue:
  - X exact matches: Correct color and correct position.
  - Y color matches: Correct color but in the wrong position.

You have 10 total guesses. After the game ends, you can choose to play again.


## Example
```
Enter a seed, or press Enter for a random code: 123
The secret code has been chosen. You have 10 tries to guess the code.

-----------------------------
Make a guess of four colors:
0 - red
1 - orange
2 - yellow
3 - green
4 - blue
5 - purple
-----------------------------
Guess color 1: 0
Guess color 2: 1
Guess color 3: 2
Guess color 4: 3
...
```

This was developed for educational purposes.

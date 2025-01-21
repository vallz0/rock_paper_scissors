# Rock-Paper-Scissors Game

A simple yet engaging Rock-Paper-Scissors game built in Python, designed to demonstrate the basics of object-oriented programming and Python functionality. This project is beginner-friendly but also introduces some slightly advanced concepts like static methods and type annotations.

## Features

- **User Interaction:** The game accepts user input to play.
- **Randomized Choices:** The computer's choice is randomized for fairness.
- **Static Method:** Demonstrates the use of static methods for a game logic.
- **Type Annotations:** Ensures code clarity and reliability.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/vallz0/rock_paper_scissors.git
```

2. Navigate to the project directory:

```bash
cd 'rock_paper_scissors'
```

3. Run the `main.py` script:

```bash
python main.py
```

## How to Play

1. When prompted, type your choice (`rock`, `paper`, or `scissors`) in Portuguese (`pedra`, `papel`, or `tesoura`).
2. The program will compare your choice against the computer's choice.
3. The outcome (win, lose, or draw) will be displayed.

## Code Structure

- `game.py`
  - Contains the `Game` class with the game logic.
  - Implements a static method `start_game` to process the game flow.

- `main.py`
  - Handles user input and initializes the game logic from `game.py`.

## Example Gameplay

```plaintext
Choose rock, paper or scissors: paper
You chose: paper
The computer chose: rock
You win!
```

## Requirements

- Python 3.7 or higher

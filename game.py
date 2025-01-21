import random

class Game:
    @staticmethod
    def start_game(user_choice: str) -> None:
        valid_choices: list[str] = ["rock", "paper", "scissors"]
        if user_choice not in valid_choices:
            print("Invalid choice! Please choose between 'rock', 'paper' or 'scissors'.")
            return

        choices: list[str] = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("Draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

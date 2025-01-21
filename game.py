import random

class Game:
    @staticmethod
    def start_game(self, user_choice: str) -> None:
        valid_choices:list[str] = ["pedra", "papel", "tesoura"]
        if user_choice not in valid_choices:
            print("Escolha inválida! Por favor, escolha entre 'pedra', 'papel' ou 'tesoura'.")
            return

        choices:list[str] = ["pedra", "papel", "tesoura"]
        computer_choice = random.choice(choices)
        print(f"Você escolheu: {user_choice}")
        print(f"O computador escolheu: {computer_choice}")

        if user_choice == computer_choice:
            print("Empate!")
        elif (user_choice == "pedra" and computer_choice == "tesoura") or \
             (user_choice == "tesoura" and computer_choice == "papel") or \
             (user_choice == "papel" and computer_choice == "pedra"):
            print("Você venceu!")
        else:
            print("Você perdeu!")
from game import Game

def main():
    game = Game()

    user_input = str(input("Escolha pedra, papel ou tesoura: ")).lower()
    game.start_game(user_input)

if __name__ == "__main__":
    main()
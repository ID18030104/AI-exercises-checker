import random

class Game:
    def get_user_item(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            else:
                print("Invalid choice. Please choose again.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

        return result


#from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice in ['1', '2', '3']:
        return choice
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        return get_user_menu_choice()

def print_results(results):
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()

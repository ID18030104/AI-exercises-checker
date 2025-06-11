import random

def number_guessing_game():
    
    random_number = random.randint(1, 100)
    
    
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.")
    print("-" * 40)
    
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        
        try:
            
            guess = int(input("Enter your guess: "))
            
            
            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it correctly!")
                print(f"The number was {random_number}.")
                print(f"You won in {attempt} attempt(s)!")
                return  
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    
    print(f"\n Sorry! You've used all {max_attempts} attempts.")
    print(f"The correct number was {random_number}.")
    print("Better luck next time!")


if __name__ == "__main__":
    number_guessing_game()
    
    
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y' or play_again == 'yes':
            print("\n" + "="*50)
            number_guessing_game()
        elif play_again == 'n' or play_again == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
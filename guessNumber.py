import random

def intro():
    """Introduction to the game."""
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 200.")
    print("Can you guess it? You have 6 attempts!")

def guess_number_game():
    """Core function of the guessing game."""
    number_to_guess = random.randint(1, 200)
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 200:
                print("Your guess is out of range! Please pick a number between 1 and 200.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("That's not a valid number. Please enter a number between 1 and 200.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

def main():
    """Main function to run the game."""
    play_again = "yes"
    while play_again.lower() in ("yes", "y"):
        intro()
        guess_number_game()
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()

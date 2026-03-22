import random

def get_difficulty():
    
    print("Please select the difficulty level:")
    print("1.Easy (10 chances)")
    print("2.Medium (5 chances)")
    print("3.Hard (2 chances)")

    choice = int(input("Enter your choice: ")) 

    if choice == 1:
        print("Great! You have selected the Easy difficulty level. You have 10 chances to guess the correct number.")
        return 10
    elif choice == 2:
        print("Great! You have selected the Medium difficulty level. You have 5 chances to guess the correct number.")
        return 5
    elif choice == 3:
        print("Great! You have selected the Hard difficulty level. You have 2 chances to guess the correct number.")
        return 2
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 5
    
def play_again():
    continue_game = input("Do you want to play again? ")
    if continue_game == "yes":
        play_game()
    else:
        return

def play_game():
    computer_choice = random.randint(1,100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    chances = get_difficulty()

    print("Lets start the game!")
    attempts = 0

    for _ in range(chances):
        
        guess_number = int(input("Enter your guess: "))
        
        attempts = attempts + 1

        if guess_number > computer_choice:
            print(f"Incorrect! The number is less than {guess_number}.")
        elif guess_number < computer_choice:
            print(f"Incorrect! The number is greater than {guess_number}.")
        elif guess_number == computer_choice:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return
        
    if attempts == chances:
            print(f"You lost. The correct number is {computer_choice}")


play_game()
play_again()



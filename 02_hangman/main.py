import random

from hangman_art import hangman_stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

display_word_list = ["_"] * len(chosen_word)

def has_user_won(space):
    if "_" not in space:
        return True
    return False

print(logo)

lives = 6
while True:
    display_word = "".join(display_word_list)
    print(f"Word to guess: {display_word}")
    guess_letter = input("Guess a letter: ")
    if guess_letter in display_word_list:
        print("You have already typed this letter")
    elif guess_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess_letter:
                display_word_list[i] = guess_letter
        print("".join(display_word_list))
        win_check = has_user_won(display_word_list)
        
        if win_check:
            print("You won!!")
            print(f"**********{lives}/6 LIVES LEFT************")
            break
            
    else:
        lives -= 1
        print(f"You guessed {guess_letter}, thats not in the word. You lose a life")
        print(hangman_stages[6-lives])
        print(f"**********{lives}/6 LIVES LEFT************")
    
    # check if user has lost
    if lives == 0:
        print(f"*************It was {chosen_word}! you lose************")
        break  
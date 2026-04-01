import random
from move import Move

class Player:

    def __init__(self, is_human = True):
        self._is_human = is_human
        if is_human:
            self._marker = "X"
        else:
            self._marker = "O"

    @property
    def is_human(self):
        return self._is_human
    
    @property
    def marker(self):
        return self._marker
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input("Enter a number from (1-9)"))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move
    
    def get_computer_move(self):
        computer_choice = random.randint(1,9)
        move = Move(computer_choice)
        print("Computermove (1-9):", move.value)
        return move

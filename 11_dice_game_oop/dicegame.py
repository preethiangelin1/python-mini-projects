class DiceGame:
 
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
 
    def play(self):
        print("Welcome to dice game!!")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
 
    def play_round(self):
        print("\n------ New Round ------")

        player_value = self.player.roll_die()
        computer_value = self.computer.roll_die()
 
        self.show_dice(player_value, computer_value)
 
        if player_value > computer_value:
            print("You won this round!")
            self.player.decrement_counter()
        elif computer_value > player_value:
            print("The computer won this round.Try again.")
            self.computer.decrement_counter()
        else:
            print("It's a tie!")
 
        self.show_counters()
 
 
    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}\n")
 
    def show_counters(self):
        print(f"\nYour counter: {self.player.counter}")
        print(f"Computer counter: {self.computer.counter}")
 
    def check_game_over(self):
        if self.player.counter == 0:
            self.show_game_over(winner=self.player)
            return True
        elif self.computer.counter == 0:
            self.show_game_over(winner=self.computer)
            return True
        else:
            return False
     
    def show_game_over(self, winner):
        if winner._is_computer:
            print("Game Over. Computer won the game")
        else:
            print("Game over. You won the game, Congratulations!!")

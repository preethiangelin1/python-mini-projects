from die import Die
from player import Player
from dicegame import DiceGame

player_die = Die()
computer_die = Die()
 
my_player = Player(player_die)
computer_player = Player(computer_die, True)
 
game = DiceGame(my_player, computer_player)
 
game.play()



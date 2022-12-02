# so essentially, we can use the same method name for different classes
# this is called duck typing (if it walks like a duck and quacks like a duck, it's a duck)
# it means that we don't care about the type of the object, we only care about the methods it has
# this is a very powerful concept in Python
import random


class Player:
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_rate(self):
        return self.victories / self.games_played


class NewPlayer(Player):
    def make_move(self):
        print("I'm making a move")


class ComputerPlayer(Player):
    def make_move(self):
        print("Running some complex algorithm to find the best move")


hp = NewPlayer(100, 80)
print(hp.win_rate)
cp = ComputerPlayer(100, 20)
print(cp.win_rate)

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move()  # whoever starts first we know they have the make_move method

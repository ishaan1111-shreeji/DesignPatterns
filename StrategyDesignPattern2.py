# Changing Strategy among Rock,paper,Scissors,Random
import random
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass


# concrete classes for selection
class Rock(Strategy):
    # in actual algoithim would be replaced by methods
    def selection(self) -> str:
        return "Rock"


class Paper(Strategy):
    def selection(self) -> str:
        return "Paper"


class Scissors(Strategy):
    def selection(self) -> str:
        return "Scissors"


class Random(Strategy):
    def selection(self) -> str:
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)


class Game:
    strategy = Strategy

    def __init__(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec) -> None:
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("It's a tie")
        elif s1 == "Rock":
            if s2 == "Scissors":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Scissors":
            if s2 == "Paper":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Paper":
            if s2 == "Rock":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")


if __name__ == "__main__":
    player1 = Game(Paper())  #player 1 selects its strategy
    player2=Game(Rock())     #player 2 selects its strategy
    player1.play(player2)    #after choices done call play method
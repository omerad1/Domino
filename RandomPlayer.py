import random
import copy
from Player import Player


class RandomPlayer(Player):
    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        """ this method make one play for random player, random player first shuffle his hand and then
        place the first domino stone that he can put in the
        board. he tries to put the stone in the right side and then in the left side.
        :param board: (Board) board
        :return:(bool) True if the player has placed the domino stone and False if he didn't
        """
        x = copy.deepcopy(self.hand.dominoes)
        random.shuffle(x)
        for i in range(len(x)):
            if board.add_right(x.__getitem__(i)):
                want_to_delete = (x[i])
                self.hand.remove_domino(want_to_delete)
                return True
            else:
                if board.add_left(x.__getitem__(i)):
                    want_to_delete = (x[i])
                    self.hand.remove_domino(want_to_delete)
                    return True
        return False

    def __init__(self, name, age, hand):
        Player.__init__(self, name, age, hand)
        self.name = name
        self.age = age
        self.hand = hand

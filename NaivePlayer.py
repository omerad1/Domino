from Player import Player


class NaivePlayer(Player):
    def __init__(self, name, age, hand):
        """
        constructor
        :param name:(str) player's name
        :param age: (int) player's age
        :param hand: (Hand) player's hand
        """
        Player.__init__(self, name, age, hand)
        self.name = name
        self.age = age
        self.hand = hand

    def play(self, board):
        """
        this method make one play for naive player, naive player place the first domino stone that he can put in the
        board. he tries to put the stone in the right side and then in the left side.
        :param board: (Board) board
        :return:(bool) True if the player has placed the domino stone and False if he didn't

        """
        for j in self.hand.dominoes:
            if board.add_right(j):
                self.hand.dominoes.remove(j)
                return True
            if board.add_left(j):
                self.hand.dominoes.remove(j)
                return True
        return False

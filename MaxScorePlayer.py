import copy

from Player import Player


class MaxScorePlayer(Player):
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
        this method make one play for max score player, max score player first find the max score domino in  his hand
        and then place the first domino stone that he can put in the board.
        he tries to put the stone in the right side and then in the left side.
        :param board: (Board) board
        :return:(bool) True if the player has placed the domino stone and False if he didn't
        """
        sorted_list = []
        x = copy.deepcopy(self.hand.dominoes)
        while x:
            max_value = x[0].left + x[0].right
            removing = x[0]
            for d in x:
                domino_sum = d.left + d.right
                if domino_sum > max_value:
                    max_value = domino_sum
                    removing = d
            sorted_list.append(removing)
            x.remove(removing)
        for j in sorted_list:
            if board.add_right(j):
                self.hand.dominoes.remove(j)
                return True
            if board.add_left(j):
                self.hand.dominoes.remove(j)
                return True
        return False

    def __str__(self):
        """
        string that represents the player
        :return: (str) string by the next format: Name:, Age:, Hand: ,Score:
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {str(self.hand)}, Score: {self.score()}, I can win the game!'

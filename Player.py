import copy


class Player:
    """
    this class represents player in the domino game
    """

    def __init__(self, name, age, hand):
        """
        constructor
        :param name:(str) player's name
        :param age: (int) player's age
        :param hand: (Hand) player's hand
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        method that represents the score of the player - the sum of the values of the domino stone in the player's hand
        :return:(int) score
        """
        score_inv = 0
        if len(self.hand) == 0:
            return copy.deepcopy(score_inv)
        for i in range(len(self.hand)):
            score_inv += self.hand.__getitem__(i).left \
                         + self.hand.__getitem__(i).right  # TODO check if that's ok that the score is sums up
        return copy.deepcopy(score_inv)

    def has_dominoes(self):
        """
        method the checks if the player has left domino stones in his hand
        :return:(bool) True if he has left domino stones and False if he isn't
        """
        if len(self.hand.dominoes) > 0:
            return True
        else:
            return False

    def play(self, board):
        """
        not implemented here
        :param board: game board
        :return:
        """
        pass

    def __str__(self):
        """
        string that represents the player
        :return: (str) string by the next format: Name:, Age:, Hand: ,Score:
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {str(self.hand)}, Score: {self.score()}'

    def __repr__(self):
        """
        same as str
        :return: (str)
        """
        return str(self)

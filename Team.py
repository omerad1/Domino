import copy


class Team:
    def __init__(self, name, players):
        """
        constructor
        :param name: (str) group name
        :param players: (list) list of the players
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
        the method will return list of the players
        :return: (list) copy of the players list
        """
        return copy.deepcopy(self.__players)

    def score_team(self):
        """
        this method sums up the score of all the team players
        :return:(int) total score of the team
        """
        total_score = 0
        for i in self.__players:
            total_score += i.score()
        return total_score

    def has_dominoes_team(self):
        """
        this method checks if left at least one player with dominoes stones
        :return: (bool) True if yes and False if no
        """
        for i in self.__players:
            if i.has_dominoes():
                return True
        return False

    def play(self, board):
        """
        this method makes only one play for the team(only one player is playing)
        the method checks every player from the beginning, if the player can add domino stone to the board so that's it
         and if not she checks the next play and further on
        :return:(bool) True if the team played and False if isn't
        """
        for i in self.__players:
            if i.play(board):
                return True
        return False

    def __str__(self):
        """
        represents the team
        :return: (str) the team
        """
        return f'Name {self.name}, Score team: {self.score_team()}, Players: {(" ".join(str(i) for i in self.get_team()))}'

    def __repr__(self):
        """
        represents the team
        :return: (str) the team
        """
        return str(self)

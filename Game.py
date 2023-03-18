class Game:
    """
    defining the game itself
    """

    def __init__(self, board, team1, team2):
        """
         constructor
        :param board:(Board) domino game board
        :param team1:(Team) team
        :param team2:(Team) team
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def scorer(self):
        score_1 = self.team1.score_team()
        score_2 = self.team2.score_team()
        if score_1 < score_2:
            return f'Team {self.team1.name} wins Team {self.team2.name}'
        if score_2 < score_1:
            return f'Team {self.team2.name} wins Team {self.team1.name}'
        if score_2 == score_1:
            return "Draw!"

    def play(self):
        """
        method that controls the game
        there is two teams, team1 and team2, first team1 plays and then team2
        every team in her turn try to add domino stone to the board, the game ends when one of the teams is out
        of domino stones.
        :return:(str) string that represents the team that won, winning team defines by the lower score
        """
        i = 0
        while self.team1.has_dominoes_team and self.team2.has_dominoes_team:  # when the teams has left domino stones
            if i == len(self.team1.get_team()):
                i = 0
            if len(self.board) == self.board.max_capacity:
                return self.scorer()
            if not self.team1.play(self.board) or not self.team2.play(self.board):
                return self.scorer()
            self.team1.play(self.board)
            self.team2.play(self.board)
            i += 1
        return self.scorer()

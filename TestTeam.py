from unittest import TestCase
from Team import Team
from Player import Player
from Hand import Hand
from Domino import Domino
from Board import Board
from NaivePlayer import NaivePlayer
from MaxScorePlayer import MaxScorePlayer


class TestTeam(TestCase):

    def test_get_team(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        board = Board(11)
        board.add(d1)
        board2 = Board(23)
        board2.add(d2)  # [3,1]
        board.add(d2)  # [5,1],[1,3])
        p3 = Player('f', "f", h3)
        p2 = Player('omer', '25', h1)
        p = Player('omer', '25', h)
        team = Team("winners", [p, p2, p3])
        self.assertEqual(str(team.get_team()), str([p, p2, p3]))  # [Name: omer, Age: 25, Hand: [1|5], Score: 6, Name: omer,
        # Age: 25, Hand: [1|5], Score: 6, Name: f, Age: f, Hand: [2|2][3|1][1|5][1|1], Score: 16]
        print(team.get_team())

    def test_score_team(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        h2 = Hand([Domino(4, 4)])
        h4 = Hand([d4])
        board = Board(11)
        board.add(d1)
        board2 = Board(23)
        board2.add(d2)  # [3,1]
        board.add(d2)  # [5,1],[1,3])
        p4 = Player('f', "f", h4) # 6
        p3 = Player('f', "f", h3) #16
        p2 = Player('omer', '25', h1) #6
        p = Player('omer', '25', h)
        p1 = Player('om', '23', h2) #8
        team = Team("winners", [p, p2, p3])
        team2 = Team('losers', [p1])
        team3 = Team("wo",[p1,p2,p3,p4])
        self.assertEqual(team.score_team(), 28)
        self.assertEqual(team2.score_team(), 8)
        self.assertEqual(team3.score_team(),36)

    def test_has_dominoes_team(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        h2 = Hand([])
        h4 = Hand([d4])
        board = Board(11)
        board.add(d1)
        board2 = Board(23)
        board2.add(d2)  # [3,1]
        board.add(d2)  # [5,1],[1,3])
        p4 = Player('f', "f", h4)
        p3 = Player('f', "f", h3)
        p2 = Player('omer', '25', h1)
        p = Player('omer', '25', h)
        p1 = Player('om', '23', h2)
        team = Team("winners", [p, p2, p3])
        team2 = Team('', [p1])
        self.assertTrue(team.has_dominoes_team())
        self.assertFalse(team2.has_dominoes_team())

    def test_play_team(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        h2 = Hand([])
        h4 = Hand([d4])
        board = Board(11)
        board.add(d1)
        board2 = Board(23)
        board2.add(d2)  # [3,1]
        board.add(d2)  # [5,1],[1,3])
        p4 = Player('f', "f", h4)
        p3 = Player('f', "f", h3)
        p2 = MaxScorePlayer('omer', '25', h1)
        p = NaivePlayer('omer', '25', h)
        p1 = Player('om', '23', h2)
        team = Team("winners", [p, p2, p3])
        team2 = Team('', [p1])
        self.assertTrue(team.play(board))
        self.assertFalse(team2.play(board2))

    def test_str_team(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        h2 = Hand([d2])
        h4 = Hand([d4])
        board = Board(11)
        board.add(d1)
        board2 = Board(23)
        board2.add(d2)  # [3,1]
        board.add(d2)  # [5,1],[1,3])
        p4 = Player('f', "f", h4)
        p3 = Player('f', "f", h3)
        p2 = Player('omer', '25', h1)
        p = Player('omer', '25', h)
        p1 = Player('om', '23', h2)
        team = Team("winners", [p1, p2])
        team2 = Team('losers', [p1])
        self.assertEqual(team2.score_team(), 4)
        self.assertEqual(str(team2), "Name losers, Score team: 4, Players: Name: om, Age: 23, Hand: [3|1], Score: 4")
        self.assertEqual(str(team), str(team))
        self.assertNotEqual(str(team2), str(team))

    def test_repr(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3, 3)
        h = Hand([d1])
        h3 = Hand([Domino(2, 2), d2, d1, d3])
        p = Player('omer', '25', h)
        p1 = Player('om', '23', h3)
        team = Team("winners", [p, p1])
        self.assertEqual(str(team), repr(team))


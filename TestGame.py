import random
from unittest import TestCase
from MaxScorePlayer import MaxScorePlayer
from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team
from unittest import TestCase
from RandomPlayer import RandomPlayer


class TestGame(TestCase):

    def test_play(self):
        d1 = Domino(2, 3)
        d2 = Domino(4, 3)
        d3 = Domino(5, 5)
        d4 = Domino(6, 1)
        d5 = Domino(4, 1)
        d6 = Domino(6, 2)
        h1 = Hand([d1, d2, d3])
        h2 = Hand([d2, d4, d3])
        h3 = Hand([d4, d6, d1])
        h4 = Hand([d2, d3, d5])
        h5 = Hand([d4, d5, d6])
        h6 = Hand([d4, d2, d6])
        p1 = NaivePlayer('omer', "25", h1)
        p2 = NaivePlayer('omer', "25", h2)
        p3 = NaivePlayer('omer', "25", h3)
        p4 = NaivePlayer('omer', "25", h4)
        p5 = NaivePlayer('omer', "25", h5)
        p6 = NaivePlayer('omer', "25", h6)
        b = Board(18)
        t1 = Team("Winners", [p1, p2, p3])
        t2 = Team("Losers", [p4, p5, p6])
        g = Game(b, t1, t2)
        self.assertEqual("Team Losers wins Team Winners", g.play())
        h3 = Hand([d2, d2, d1])
        h4 = Hand([d2, d5, d5])
        h5 = Hand([d5, d5, d6])
        p1 = NaivePlayer('omer', "25", h1)
        p2 = MaxScorePlayer('omer', "25", h2)
        p3 = RandomPlayer('omer', "25", h3)
        p4 = MaxScorePlayer('omer', "25", h4)
        p5 = RandomPlayer('omer', "25", h5)
        p6 = MaxScorePlayer('omer', "25", h6)
        t1 = Team("Winners", [p1, p2, p3])
        t2 = Team("Losers", [p4, p5, p6])
        g2 = Game(b, t1, t2)
        b2 = Board(5)
        self.assertEqual("Team Winners wins Team Losers", g2.play())
        g3 = Game(b2, t1, t2)
        g4 = Game(b, t1, t1)
        self.assertEqual("Team Winners wins Team Losers", g3.play())
        self.assertEqual("Draw!", g4.play())

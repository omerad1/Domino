from Domino import Domino
from Hand import Hand
from Board import Board
from RandomPlayer import RandomPlayer
from unittest import TestCase


class TestRandomPlayer(TestCase):
    def test_play(self):
        d1 = Domino(2, 1)
        d2 = Domino(3, 2)
        d3 = Domino(5, 3)
        d4 = Domino(6, 4)
        board = Board(7)
        board.add(d1)
        h = Hand([d1, d2, d3, d4])
        p = RandomPlayer("omer", "25", h)
        print(p.hand.dominoes)
        self.assertTrue(p.play(board))
        print(p.hand.dominoes)
        self.assertTrue(p.play(board))
        print(p.hand.dominoes)
        self.assertTrue(p.play(board))
        print(p.hand.dominoes)
        h1 = Hand([d2,d3]) #([3,2],[5,3])
        board1 =Board(4)
        board1.array = [Domino(3,4)]
        p1 = RandomPlayer('','',h1)
        self.assertTrue(p1.play(board1))
        self.assertFalse(p1.play(board1))
    def test_repr(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = RandomPlayer('omer', '25', h)
        self.assertEqual('Name: omer, Age: 25, Hand: [5|1][3|1], Score: 10', repr(p))

    def test_str_Player(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        h = Hand([d1, d2, d3])
        p1 = RandomPlayer("shir", 26, h)
        self.assertEqual(str(p1), "Name: shir, Age: 26, Hand: [1|2][1|3][1|4], Score: 12")

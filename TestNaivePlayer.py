from Domino import Domino
from Hand import Hand
from Board import Board
from NaivePlayer import NaivePlayer
from unittest import TestCase


class TestNaivePlayer(TestCase):
    def test_play(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(1,1)
        h = Hand([d1])
        h1 = Hand([d1])
        h3 = Hand([Domino(2,2),d2,d1,d3])
        h2 = Hand([Domino(4, 4)])
        board = Board(5)
        board.add(d1)
        board.add(d2)  # [5,1],[1,3])
        p3 = NaivePlayer('f',"f",h3)
        p2 = NaivePlayer('omer', '25', h1)
        p = NaivePlayer('omer', '25', h)
        p1 = NaivePlayer('om', '23', h2)
        self.assertTrue(p.play(board))
        self.assertTrue(p2.play(board))
        self.assertFalse(p1.play(board))
        self.assertTrue(p3.play(board))


    def test_str(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = NaivePlayer('omer', '25', h)
        self.assertEqual('Name: omer, Age: 25, Hand: [5|1][3|1], Score: 10', str(p))

    def test_repr(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = NaivePlayer('omer', '25', h)
        self.assertEqual('Name: omer, Age: 25, Hand: [5|1][3|1], Score: 10', repr(p))

    def test_str_Player(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        h = Hand([d1, d2, d3])
        p1 = NaivePlayer("shir", 26, h)
        self.assertEqual(str(p1), "Name: shir, Age: 26, Hand: [1|2][1|3][1|4], Score: 12")


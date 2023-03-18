from unittest import TestCase
from Player import Player
from Hand import Hand
from Domino import Domino
from Board import Board
class TestPlayer(TestCase):
    def test_init(self):
        n1 = "omer"
        a1 = "23"
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        h = Hand([d1, d2, d3])
        p = Player(n1,a1,h)
        self.assertEqual(p.name,"omer")
        self.assertEqual(p.age, "23")
        self.assertEqual(p.hand, h)

    def test_score(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        h = Hand([d1, d2, d3])
        h1 = Hand([d3, d3, d3])
        h2 = Hand([d1, d2, d2, d2, d1])
        h4 = Hand([])
        p = Player('omer', '25', h)
        p1 = Player('hila', '25', h1)
        p3 = Player("", "", h2)
        p4 = Player("", "", h4)
        self.assertEqual(p4.score(), 0)
        self.assertEqual(p1.score(), p.score())
        self.assertEqual(p.score(), 15)
        self.assertNotEqual(p.score(), 13)
        self.assertEqual(p1.score(), 15)
        self.assertNotEqual(p.score(), 13)
        self.assertEqual(p1.score(), 15)
        self.assertEqual(p3.score(), 24)
        self.assertEqual(p4.score(), 0)
        d1 = Domino(2, 3)
        d2 = Domino(4, 3)
        d3 = Domino(5, 5)
        d4 = Domino(6, 1)
        d5 = Domino(4, 1)
        d6 = Domino(6, 2)
        h1 = Hand([d1, d2, d3])  # [2|3][4|3][5|5]
        h2 = Hand([d2, d4, d3])  # [4|3][6|1][5|5]
        h3 = Hand([d4, d6, d1])  # [6|1][6|2][2|3]
        h4 = Hand([d2, d3, d5])  # [4|3][5|5][4|1]
        h5 = Hand([d4, d5, d6])  # [6|1][4|1][6|2]
        h6 = Hand([d4, d2, d6])  # [6|1][4|3][6|2]
        p1 = Player('omer', "25", h1)
        p2 = Player('omer', "25", h2)
        p3 = Player('omer', "25", h3)
        p4 = Player('omer', "25", h4)
        p5 = Player('omer', "25", h5)
        p6 = Player('omer', "25", h6)
        self.assertEqual(p1.score(),22)
        self.assertEqual(p2.score(), 24)
        self.assertEqual(p3.score(), 20)
        self.assertEqual(p4.score(), 22)
        self.assertEqual(p5.score(), 20)
        self.assertEqual(p6.score(), 22)

    def test_play(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = Player('omer', '25', h)
        self.assertEqual(p.play(Board(3)),None)
    def test_has_dominoes(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = Player('omer', '25', h)
        self.assertTrue(p.has_dominoes())
        p.hand.remove_domino(d1)
        p.hand.remove_domino(d2)
        self.assertFalse(p.has_dominoes())

    def test_str(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = Player('omer', '25', h)
        self.assertEqual('Name: omer, Age: 25, Hand: [5|1][3|1], Score: 10', str(p))

    def test_repr(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        h = Hand([d1, d2])
        p = Player('omer', '25', h)
        self.assertEqual('Name: omer, Age: 25, Hand: [5|1][3|1], Score: 10', repr(p))

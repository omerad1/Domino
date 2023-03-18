from Domino import Domino
from Hand import Hand
from Board import Board
from MaxScorePlayer import MaxScorePlayer
from unittest import TestCase


class TestMaxScorePlayer(TestCase):

    def testPlay(self):
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(1, 1)
        d4 = Domino(3,3)
        d5 = Domino(5,2)
        d6 = Domino(5,1)
        h1 = Hand([d1,d2,d3])  # [1|5][3|1][1|1]
        h2 = Hand([d4])
        h3 = Hand([d2,d3,d5])# [3|3]
        h4 = Hand([d3,d5,d2,d6]) # [3|1][1|1][5|2]
        board1 = Board(19)
        board2 = Board(21)
        board1.add(d1) # [1|5]
        board2.add(d2)
        board2.add(d3) # [3|1][1|1]
        p1 = MaxScorePlayer('omer','25',h1)
        p2 = MaxScorePlayer('omer','25',h2)
        p3 = MaxScorePlayer('omer','25',h3)
        p4 = MaxScorePlayer('omer','25',h4)
        self.assertTrue(p3.play(board1))# works
        self.assertTrue(p4.play(board2))
        self.assertFalse(p2.play(board1))
        self.assertTrue((p1.play(board2)))


    def test_str_Player(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        h = Hand([d1, d2, d3])
        p1 = MaxScorePlayer("shir", 26, h)
        self.assertEqual(str(p1), "Name: shir, Age: 26, Hand: [1|2][1|3][1|4], Score: 12, I can win the game!")

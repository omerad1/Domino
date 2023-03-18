
from unittest import TestCase
from Board import Board
from Domino import Domino
from Exceptions import InvalidNumberException
from Exceptions import EmptyBoardException
from Exceptions import FullBoardException


class TestBoard(TestCase):
    def test_init_Board(self):
        self.assertRaises(InvalidNumberException, Board, 0)
        self.assertEqual([], Board(1).get_collection())

    def test_in_left(self):
        d = Board(3)
        b = Board(3)
        d1 = Domino(1, 5)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        b.add_left(d1)
        b.add_left(d2)
        b.add_left(d3)
        with self.assertRaises(EmptyBoardException):
            d.in_left()
        self.assertEqual(2, b.in_left(), "failed")

    def test_in_right(self):
        b = Board(8)
        b3 = Board(1)
        d1 = Domino(1, 5)
        d3 = Domino(3, 5)
        d4 = Domino(6, 6)
        d5 = Domino(5, 3)
        d6 = Domino(5, 6)
        b.add_right(d1)
        b.add_right(d3)
        self.assertEqual(3, b.in_right(), "failed")
        b.add_right(d4)
        self.assertEqual(3, b.in_right(), "failed")
        b.add_right(d5)
        self.assertEqual(5, b.in_right(), "failed")
        b.add_right(d6)
        self.assertEqual(6, b.in_right(), "failed")
        with self.assertRaises(EmptyBoardException):
            b3.in_right()

    def test_add_left(self):
        d = Board(1)
        b = Board(3)
        d1 = Domino(1, 3)
        d.add(d1)
        b.add_left(d1)
        with self.assertRaises(FullBoardException):
            d.add_right(d1)
        self.assertEqual([Domino(1, 3)], b.get_collection(), "failed")

    def test_add_right(self):
        d = Board(1)
        b = Board(3)
        d1 = Domino(1, 3)
        d.add(d1)
        b.add_right(d1)
        self.assertEqual([Domino(1, 3)], b.get_collection(), "failed")
        d2 = Domino(4, 4)
        b.add_right(d2)
        self.assertEqual([Domino(1, 3)], b.get_collection(), "failed")
        with self.assertRaises(FullBoardException):
            d.add_right(d1)

    def test_contains(self):
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 3)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, True)
        self.assertEqual(True, b.__contains__(d3), "fail")
        self.assertEqual(False, b.__contains__(d4))

    def test_eq(self):
        b = Board(4)  # [(3,3)(3,4)(4,3)]
        b2 = Board(4)  # [(1,4)(4,3)(3,3)]
        b3 = Board(3)
        b4 = Board(4)  # [(3,3)(3,4)(4,3)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, False)
        b.add(d2, True)
        b2.add(d2, True)
        b2.add(d1, True)
        b2.add(d3, False)
        b3.add(d1, True)
        b3.add(d2, True)
        b3.add(d3, False)
        b4.add_right(d1)
        b4.add_right(d2)
        b4.add_right(d2)
        self.assertEqual(True, b == b4, "failed")
        self.assertEqual(False, b == b2, "failed")
        self.assertEqual(False, b == b3, "failed")
        self.assertEqual(True, b == b, "failed")
        self.assertEqual(False, b3 == b, "failed")


    def test_ne(self):
        b = Board(4)
        b2 = Board(4)
        b3 = Board(3)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, False)
        b2.add(d1, True)
        b2.add(d2, True)
        b2.add(d3, False)
        b3.add(d1, True)
        b3.add(d2, True)
        b3.add(d3, False)
        self.assertEqual(True, b != b3, "failed")
        self.assertEqual(False, b != b2, "failed")
        self.assertEqual(True, b3 != b, "failed")

    def test_getitem(self):
        b = Board(4)
        b2 = Board(4)
        b3 = Board(3)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, False)
        self.assertEqual(d1, b.__getitem__(0))
        self.assertEqual(None, b.__getitem__(5))

    def test_len(self):
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, True)
        self.assertEqual(3, len(b), "failed")

    def test_str(self):
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, True)
        self.assertEqual('[3|3][3|4][4|1]', str(b), "failed")


    def test_repr(self):
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        b.add(d1, True)
        b.add(d2, True)
        b.add(d3, True)
        self.assertEqual('[3|3][3|4][4|1]', b.__repr__(), "failed")

    def test_Board(self):
        """ Test for str, len, repr and add"""
        b = Board(4)
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 3)
        d5 = Domino(1, 1)

        self.assertTrue(b.add(d1, False))
        self.assertEqual(len(b), 1)
        self.assertEqual(str(b), '[3|3]')
        self.assertEqual(repr(b), '[3|3]')

        self.assertTrue(b.add(d2, False))
        self.assertEqual(len(b), 2)
        self.assertEqual(str(b), '[4|3][3|3]')
        self.assertEqual(repr(b), '[4|3][3|3]')

        self.assertTrue(b.add(d3, False))

        self.assertEqual(len(b), 3)
        self.assertEqual(str(b), '[1|4][4|3][3|3]')
        self.assertEqual(repr(b), '[1|4][4|3][3|3]')

        self.assertTrue(b.add(d4, True))

        self.assertEqual(len(b), 4)
        self.assertEqual(str(b), '[1|4][4|3][3|3][3|1]')
        self.assertEqual(repr(b), '[1|4][4|3][3|3][3|1]')

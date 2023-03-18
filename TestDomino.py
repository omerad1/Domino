from unittest import TestCase
from Domino import Domino
from Exceptions import InvalidNumberException


class TestDomino(TestCase):
    def test_init(self):
        self.assertRaises(InvalidNumberException, Domino, 22, -10)
        self.assertRaises(InvalidNumberException,Domino,4,55)

    def test_get_left(self):
        a = Domino(3, 4)
        self.assertEqual(a.get_left(), 3, "failed")

    def test_get_right(self):
        a = Domino(3, 4)
        self.assertEqual(a.get_right(), 4, "failed")

    def test_str(self):
        a = Domino(3, 4)
        b = Domino(2, 1)
        self.assertEqual(a.__str__(), "[3|4]", "failed")
        self.assertEqual(b.__str__(), "[2|1]", "failed")


    def test_repr(self):
        a = Domino(3, 4)
        b = Domino(2, 1)
        self.assertEqual(a.__repr__(), "[3|4]", "failed")
        self.assertEqual(b.__repr__(), "[2|1]", "failed")

    def test_eq(self):
        a = Domino(3, 4)
        b = Domino(2, 1)
        c = Domino(3, 4)
        d = Domino(4, 3)
        e = Domino(3, 5)
        self.assertEqual(a.__eq__(b), False, "failed")
        self.assertEqual(a.__eq__(c), True, "failed")
        self.assertEqual(a.__eq__(d), True, "failed")
        self.assertEqual(a.__eq__(e), False, "failed")
        self.assertEqual(a.__eq__(a), True, "failed")
        self.assertEqual(a == b, False, "failed")

    def test_ne(self):
        a = Domino(3, 4)
        b = Domino(2, 1)
        c = Domino(3, 4)
        d = Domino(4, 3)
        e = Domino(3, 5)
        self.assertEqual(a.__ne__(b), True, "failed")
        self.assertEqual(a != c, False, "failed")
        self.assertEqual(a != d, False, "failed")
        self.assertEqual(a.__ne__(e), True, "failed")

    def test_gt(self):
        d = Domino(4, 3)
        e = Domino(3, 5)
        self.assertEqual(d > e, False, "failed")
        self.assertEqual(e > d, True, "failed")

    def test_contains(self):
        a = Domino(3, 4)
        b = Domino(2, 1)
        num_a = 3
        num_b = 2
        num_c = 5
        self.assertEqual(num_a in a, True, "failed")
        self.assertEqual(a.__contains__(num_b), False , "failed")
        self.assertEqual(num_c in b, False,"failed")
        self.assertEqual(num_b in b,True,"failed")

    def test_flip(self):
        a = Domino(3,5)
        self.assertEqual(a.flip(),"[5|3]","failed")
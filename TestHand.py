import copy
from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Exceptions import NoSuchDominoException
from Board import Board


class TestHand(TestCase):
    def test_add(self):
        """

        :return:
        """
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        h = Hand([d1, d2])
        h1 = Hand([d1, d3])
        h2 = Hand([])
        self.assertEqual([d2, d1, d3], h1.add(d2, 0))
        self.assertEqual([d1, d2, d3], h.add(d3), "failed")
        self.assertEqual([d1], h2.add(d1), " :(")

    def test_remove_domino(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        d4 = Domino(1, 5)
        h = Hand([d1, d2, d3, d4])
        h1 = copy.deepcopy(h)
        h2 = Hand([d1, d2])
        self.assertEqual(1, h.remove_domino(d2), "failed")
        self.assertEqual(0, h.remove_domino(d4), "failed")
        self.assertEqual(0, h1.remove_domino(d4), "failed")
        with self.assertRaises(NoSuchDominoException):
            h2.remove_domino(d3)

    def test_get_item(self):
        d1 = Domino(5, 1)
        d2 = Domino(3, 1)
        d3 = Domino(3, 2)
        a = Hand([d1, d2, d3])
        self.assertEqual(a.__getitem__(0), Domino(5, 1), "bad index")
        self.assertEqual(a.__getitem__(1), d2, "bad index")
        self.assertEqual(a.__getitem__(2), d3, "bad index")
        self.assertEqual(None,a.__getitem__(4))

    def test_contains(self):

        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 3)
        b = Hand([d1, d2, d3, d4])
        self.assertEqual(True, b.__contains__(d3), "fail")
        self.assertEqual(True, b.__contains__(d4))
        self.assertFalse(b.__contains__(Domino(4,4)))
        self.assertTrue(b.__contains__(Domino(4,1)))

    def test_eq(self):
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(1, 4)
        d4 = Domino(3,4)
        h1= Hand([d1,d2])
        h2 = Hand([d1,d4])
        h3 = Hand([d3,d2])
        self.assertTrue(h1==h2)
        self.assertFalse(h3 == h2)
        self.assertTrue((h1==h1))
        self.assertTrue(h3 != h2)
        self.assertFalse(h1!=h2)

    def test_len(self):
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        h2= Hand([])
        h1 = Hand([d1, d2])
        self.assertEqual(len(h1),2)
        self.assertNotEqual(len(h1),33)
        self.assertEqual(len(h2),0)

    def test_str(self):
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(5,1)
        h1 = Hand([d3,d1, d2])
        self.assertEqual("[5|1][3|3][4|3]",str(h1))

    def test_repr(self):
        d1 = Domino(3, 3)
        d2 = Domino(4, 3)
        d3 = Domino(5,1)
        h1 =Hand([d3,d1,d2])
        self.assertEqual(str(h1),repr(h1))
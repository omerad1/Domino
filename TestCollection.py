from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def test_get_collection(self):
        c = Collection([1, 2, "if"])
        self.assertEqual(c.get_collection(), [1, 2, "if"], "bad input")

    def test_add(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        with self.assertRaises(NotImplementedError):
            a.add(2, 4)

    def test_getitem(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        self.assertEqual(a.__getitem__(5), "a", "bad index")
        self.assertEqual(a.__getitem__(1), 2, "bad index")
        self.assertEqual(a.__getitem__(6), "omer", "bad index")
        self.assertTrue((a.__getitem__(100),None))

    def test_eq(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        b = Collection([1, 2, 3, 4, 5, "a", "omer"])
        f = Collection([1, 2, 2, 4, 5, "a", "omer"])
        c = Collection([1, 2, 3, 4, 5, "aa", "omer"])
        b = Collection([1, 2, 3, 4, 5, "a", "omer"])
        self.assertEqual(a.__eq__(b), True, "failed")
        self.assertEqual(a.__eq__(a), True, "failed")
        self.assertEqual(a.__eq__(f), False, "failed")
        self.assertEqual(a.__eq__(c), False, "failed")

    def test_ne(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        b = Collection([1, 2, 3, 4, 5, "a", "omer"])
        f = Collection([1, 2, 2, 4, 5, "a", "omer"])
        c = Collection([1, 2, 3, 4, 5, "aa", "omer"])
        b = Collection([1, 2, 3, 4, 5, "a", "omer"])
        self.assertEqual(a.__ne__(b), False, "failed")
        self.assertEqual(a.__ne__(a), False, "failed")
        self.assertEqual(a.__ne__(f), True, "failed")
        self.assertEqual(a.__ne__(c), True, "failed")

    def test_len(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        b = Collection([1, 2, 0, 4, 5, "a", "omer"])
        f = Collection([1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 5, "a", "wwwwwwwwwwwwwwwwwwwomer"])
        c = Collection([1, 2, 3, 4, 5, "aa", "omer"])
        d = Collection([1, 2, 3, 4, 5, "a", "omer"])
        self.assertEqual(a.__len__(), 7, "bad len")
        self.assertEqual(b.__len__(), 7, "bad len")
        self.assertEqual(c.__len__(), 7, "bad len")
        self.assertEqual(f.__len__(), 13, "bad len")
        self.assertEqual(d.__len__(), 7, "bad len")

    def test_contains(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        x = [1, 2, 3, 4, 5, 6, 7, 'Tamir']
        self.assertEqual(a.__contains__(x[0]), True, f'not containing item {x[0]}')
        self.assertEqual(a.__contains__(x[7]), False, f'not containing item {x[7]} ')
        self.assertEqual(a.__contains__(88), False, f'not containing item {88} ')

    def test_str(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        x = Collection([1, 2, 3, 4, 5, 6, 7, 'Tamir'])
        self.assertEqual(a.__str__(),'12345aomer',"failed")
        self.assertEqual(x.__str__(), '1234567Tamir', "failed")

    def test_repr(self):
        a = Collection([1, 2, 3, 4, 5, "a", "omer"])
        x = Collection([1, 2, 3, 4, 5, 6, 7, 'Tamir'])
        self.assertEqual(a.__repr__(),'12345aomer',"failed")
        self.assertEqual(x.__repr__(), x.__str__(), "failed")
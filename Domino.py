import copy
from Exceptions import InvalidNumberException


class Domino:
    """
    represents domino stone
    """

    def __init__(self, left, right):
        """
        constructor
        :param left: (int) number in range [0-6] that represent the right side of the domino stone
        :param right: (int) number in range [0-6] that represent the right side of the domino stone
        """
        self.left = left
        self.right = right
        if left > 6 or left < 0:
            raise InvalidNumberException("ERROR invalid input number")
        if right > 6 or right < 0:
            raise InvalidNumberException("ERROR invalid input number")

    def get_left(self):
        """
        this method return the value of the domino's left side
        :return: (int)the value of the domino's stone left side
        """
        return copy.deepcopy(self.left)

    def get_right(self):
        """
        this method return the value of the domino's right side
        :return:(int) the value of the domino's stone right side
        """
        return copy.deepcopy(self.right)

    def __str__(self):
        """
        represents the domino stone
        :return:  (str) string of the domino stone
        """
        return f'[{self.left}|{self.right}]'

    def __repr__(self):
        """
        represents the domino stone
        :return: (str) string of the domino stone
        """
        return str(self)

    def __eq__(self, other):
        """
        checks if two domino stones are equal, they will be equal if they have the same value
        :param other: (object) object to check equalization to
        :return: (bool) True if the objects are equal and False if isn't
        """
        if self.get_right() == other.get_right() and self.get_left() == other.get_left():
            return True
        if self.get_right() == other.get_left() and self.get_left() == other.get_right():
            return True
        return False

    def __ne__(self, other):
        """
        checks if two domino stones are not equal, they will be equal if they have the same value
        :param other: (object) object to check equalization to
        :return: (bool) False if the objects are equal and True if they not equal
        """
        return not self == other

    def __gt__(self, other):
        """
        greater then
        :param other: another domino stone
        :return:  True is domino stone that represents by self bigger then domino stone represents by other
        """
        self_sum = self.get_left() + self.get_right()
        other_sum = other.get_left() + other.get_right()
        if self_sum > other_sum:
            return True
        else:
            return False

    def __contains__(self, key):
        """
        checks if key is in one of the domino stone sides
        :param key:  (int) number
        :return:  True if the domino stone contains key and False if isn't
        """
        if key == self.left or key == self.right:
            return True
        else:
            return False

    def flip(self):
        """
        this method flips the domino stone
        :return: (domino) domino stone that his origin right value is in the left side
         and the origin left side in the right
        """
        return str(Domino(self.right, self.left))

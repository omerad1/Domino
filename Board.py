from Collection import Collection
from Exceptions import InvalidNumberException
from Exceptions import EmptyBoardException
from Exceptions import FullBoardException
from Domino import Domino


class Board(Collection):
    """
    this class inherits from Collection and represents the game board
    """
    def __init__(self, max_capacity):  # Board
        """
        Constructor
        :param max_capacity: (int) number that represents the maximum number of domino stone that can be in the board
        """
        Collection.__init__(self, [])
        self.array = [] # empty array
        self.max_capacity = int(max_capacity)
        if self.max_capacity > 28 or self.max_capacity < 1:
            raise InvalidNumberException("invalid number exception")

    def in_left(self):  ###
        """
        if the board is empty it will throw Exception
        :return: the item in the left of the board
        """
        if not self.array:
            raise EmptyBoardException("the board is empty")
        else:
            return self.array.__getitem__(0).get_left()

    def in_right(self):  ###
        """
        if the board is empty it will throw Exception
        :return: the item in the right of the board
        """
        if not self.array:
            raise EmptyBoardException("the board is empty")
        else:
            return self.array.__getitem__(len(self.array) - 1).get_right()

    def add_left(self, domino):  ###
        """
        add domino stone to the left side
        :param domino: (Domino) domino stone
        :return: (bool/Exception) True if the domino stone has been successfully added and False if not,
        if the Board is full the method will throw Exception
        """
        if len(self.array) >= self.max_capacity:
            raise FullBoardException("the board is full")
        if not self.array:
            self.array.append(domino)
            return True
        if self.in_left() == domino.get_right():
            self.array.insert(0, domino)
            return True
        else:
            flipped = (Domino(domino.right, domino.left))
            if self.in_left() == flipped.get_right():
                self.array.insert(0, flipped)
                return True
        return False

    def add_right(self, domino):  ###
        """
        add domino stone to the right side
        :param domino: (Domino) domino stone
        :return: (bool/Exception) True if the domino stone has been successfully added and False if not,
        if the Board is full the method will throw Exception
        """
        if len(self.array) >= self.max_capacity:  # Exception
            raise FullBoardException("the board is full")
        if not self.array:
            self.array.append(domino) # if the Board is empty
            return True
        if self.in_right() == domino.get_left():
            self.array.append(domino)
            return True
        else:
            flipped = (Domino(domino.right, domino.left)) # flipping
            if self.in_right() == flipped.get_left():
                self.array.append(flipped)
                return True
        return False

    def add(self, domino, add_to_right=True):  ###
        """
        this method will add domino stone to the board,
        if add_to_right = True
        the method will try to add the stone to the right side of the board, else the method will try to add the stone
        to the left side of the board
        the method is using add_right and add_left in order to work
        :param domino: (Domino) domino stone
        :param add_to_right: (bool) True if the domino stone has been added
        :return: (bool/Exception) True if the domino stone has been successfully added and False if not,
        if the Board is full the method will throw Exception
        """
        if len(self.array) >= self.max_capacity:  # Exception
            raise FullBoardException("the board is full")
        if add_to_right:
            return self.add_right(domino)
        else:
            return self.add_left(domino)

    def __contains__(self, key):
        """
        checks if item is in array by __eq__ method
        :param key: (Domino) domino stone
        :return: (bool) True if the domino in array and False if isn"t
        """
        for i in self.array:
            if i.__eq__(key):
                return True
        return False

    def __eq__(self, other):  ###
        """
        checks if self and other are equal, they will be equal if their max_capacity value is equal
         and their array is equal
        :param other: (object) the object that we compare to self
        :return: (bool) True if the objects are equal and false if isn't
        """
        if self.max_capacity == other.max_capacity:
            for i in range(len(self.array) - 1):
                if (self.array[i]).get_left() != (other.array[i]).get_left() \
                        or (self.array[i]).get_right() != (self.array[i]).get_right():
                    return False
            return True
        return False

    def __ne__(self, other):  ####
        """
        checks if self and other are not equal by the therms of __eq__ method
        :param other: (object) the object that we compare to self
        :return: (bool) True if the objects are  not equal and false if they equal
        """
        return not self.__eq__(other)

class Collection:
    """
    represents an collection of objects
    """
    def __init__(self, array):
        """
        constructor
        :param array: (list) represents the list of the collection's objects
        """
        self.array = array

    def get_collection(self):
        """
        this method will return the array
        :return: (list) array
        """
        return self.array

    def add(self, item, option):
        """
        not implemented in this class
        """
        raise NotImplementedError("sub class should implement this")

    def __getitem__(self, i):
        """
        this method will return the item in the index place
        :param i: (int) index
        :return: (object) the object in the index place
        """
        try:
            return self.array[i]
        except IndexError:
            return

    def __eq__(self, other):
        """
        this method will check if 2 objects are equal
        :param other: (object) object to check equalization with
        :return: (bool) True if the objects are equal and False if they isn't
        """
        if type(self) != type(other):
            return False
        for i in range(len(self.array)):
            if self.array[i] != other.array[i]:
                return False
        return True

    def __ne__(self, other):
        """
        this method will check if 2 objects are not equal
        :param other: (object) object to check equalization with
        :return: (bool) True if the objects are not equal and False if they equal
        """
        return not self.__eq__(other)

    def __len__(self):
        """
        will return the number of objects in the array
        :return: (int) number of the objects in the array
        """
        return len(self.array)

    def __contains__(self, item):
        """
        this method will check if item is in the array.
        :param item: (object) item to check if he is in the array
        :return: (bool) True if the item is in the array and False if isn't
        """
        for i in self.array:
            if item == i:
                return True
        return False

    def __str__(self):
        """
        represents the Collection
        :return: (str) string that represents the objects
        """
        b =''
        for j in self.array:
            b +=str(j)
        return b

    def __repr__(self):
        """
        represents the Collection
        :return: (str) string that represents the objects
        """
        return str(self)


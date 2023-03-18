from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):
    """
    this class inherits from collection and represents the domino stones (hand) of the player
    """

    def __init__(self, dominoes):
        Collection.__init__(self, dominoes)
        self.dominoes = dominoes

    def add(self, domino, index=None):
        """
        the method adds domino stone to the array by the index place
        :param domino: (Domino) domino stone that we want to add to the hand
        :param index: (None/int) if index = None the domino stone will be add to the end of the array,
        else the domino stone will be added in the index place of the array and the other
         stones will move one index to the right
        :return: (bool) True for successful addition
        """
        if index is None:
            self.dominoes.append(domino)
            return self.dominoes
        else:
            self.dominoes.insert(index, domino)
            return self.dominoes

    def remove_domino(self, domino):
        """
        the method will remove domino stone from the array and will return the index of the removed domino stone,
         if the domino stone that want to be removed dont exists in the board
        :param domino:(Domino) domino stone that we want to remove
        :return: (int/exception) the index of the stone in the array or exception if we cant remove the stone
        """
        for i in range(len(self.dominoes)):
            if self.dominoes.__getitem__(i) == domino:
                del self.dominoes[i]
                return i

        raise NoSuchDominoException("There is no such domino stone in your hand")


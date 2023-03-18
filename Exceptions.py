class EmptyBoardException(Exception):
    """ When the Board is empty """
    pass


class FullBoardException(Exception):
    """ When the Board is full """
    pass


class NoSuchDominoException(Exception):
    """ When the wanted domino isn't in the collection """
    pass


class InvalidNumberException(Exception):
    def __init__(self, msg):
        self.msg = msg
    """ When the number is out of range """
    def __str__(self):
        return f'ERROR {self.msg}'

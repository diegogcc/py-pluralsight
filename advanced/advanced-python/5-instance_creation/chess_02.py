"""
Overriding __new__ to see how it works.

1. __new__(cls):    cls is the base class but in case of inheritance, 
                    it is NOT necessarilly the class enclosing the __new__ call.
"""                    
class ChessCoordinate:
    def __new__(cls, *args, **kwargs):
        """ Accepts 'cls' as the first parameter.
        __new__ is a staticmethod.
        """
        print("args =", repr(args))
        print("kwargs =", repr(kwargs))
        # There's no command in order to allocate a new object, 
        # to do so, we have to use __new__ on the ultimate base class -> object
        obj = super().__new__(cls)  # using super().__new__ instead of object.__new__ (more mantainable if base object changes)
        print("id(obj) =", id(obj)) # as the object hasn't been created yet, we cannot use repr()
        return obj      # this would be the 'self' argument in __init__()

    def __init__(self, file, rank):
        # prove that self in __init__ == obj in __new__
        print("id(self)", id(self))

        if len(file) != 1:
            raise ValueError("{} component file {!r} does not have a length of one.".format(
                             self.__class__.__name__, file))
        if file not in 'abcdefgh':
            raise ValueError("{} component file {!r} is out of range".format(
                             self.__class__.__name__, file))
        if rank not in range(1, 9):
            raise ValueError("{} component rank {!r} is out of range".format(
                             self.__class__.__name__, rank))
        self._file = file 
        self._rank = rank
    
    @property
    def file(self):
        return self._file 
    
    @property
    def rank(self):
        return self._rank
    
    def __repr__(self):
        return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)
    
    def __str__(self):
        return '{}{}'.format(self.file, self.rank)

def starting_board():
    return {'♕♖': ChessCoordinate('a', 1),
            '♕♘': ChessCoordinate('b', 1),
            '♕♗': ChessCoordinate('c', 1),
            '♕♕': ChessCoordinate('d', 1),
            '♔♔': ChessCoordinate('e', 1),
            '♔♗': ChessCoordinate('f', 1),
            '♔♘': ChessCoordinate('g', 1),
            '♔♖': ChessCoordinate('h', 1),
            '♕♖♙': ChessCoordinate('a', 2),
            '♕♘♙': ChessCoordinate('b', 2),
            '♕♗♙': ChessCoordinate('c', 2),
            '♕♕♙': ChessCoordinate('d', 2),
            '♔♔♙': ChessCoordinate('e', 2),
            '♔♗♙': ChessCoordinate('f', 2),
            '♔♘♙': ChessCoordinate('g', 2),
            '♔♖♙': ChessCoordinate('h', 2),
            '♛♜': ChessCoordinate('a', 8),
            '♛♞': ChessCoordinate('b', 8),
            '♛♝': ChessCoordinate('c', 8),
            '♛♛': ChessCoordinate('d', 8),
            '♚♚': ChessCoordinate('e', 8),
            '♚♝': ChessCoordinate('f', 8),
            '♚♞': ChessCoordinate('g', 8),
            '♚♜': ChessCoordinate('h', 8),
            '♛♜♟': ChessCoordinate('a', 7),
            '♛♞♟': ChessCoordinate('b', 7),
            '♛♝♟': ChessCoordinate('c', 7),
            '♛♛♟': ChessCoordinate('d', 7),
            '♚♚♟': ChessCoordinate('e', 7),
            '♚♝♟': ChessCoordinate('f', 7),
            '♚♞♟': ChessCoordinate('g', 7),
            '♚♜♟': ChessCoordinate('h', 7),
        }

if __name__ == "__main__":
    white_queen = ChessCoordinate('d', 4)
    print(white_queen)

    # __init__'s self == __new__'s obj 
    # id(obj) = 4351035792
    # id(self) 4351035792

    boards = [starting_board() for _ in range(1)]
    # python will allocate ~18Mb in memory

    boards = [starting_board() for _ in range(10000)]
    # python will allocate ~85Mb in memory for the 320000 instances of ChessCoordinate (32 per board)
    # If the piece changes position, a new instance is created
    #       BUT we should never need more than 64 instances in total for each position in the chess board.
    #       in our case, we should never need more than the 32 initial occupied positions.
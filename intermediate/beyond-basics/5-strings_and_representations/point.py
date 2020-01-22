'''
    repr():
        - Exactness over friendliness.
        - suited for debugging.
        - generally best for logging.
        - needs to have more information.

        -> repr() is intended for developers.

    str():
        - Readable, human-friendly information.

        -> str() is intended for clients.
'''
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        ''' repr() should be a representation of the object
            it states the TYPE and the VALUES it holds.
        '''
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return '[Formatted point: {}, {}, {}]'.format(self.y, self.x, f)
        else:
            return '[Formatted point: {}, {}, {}]'.format(self.x, self.y, f)

if __name__ == "__main__":
    p = Point2D(3, 4)
    print(str(p))       # (3, 4)
    print(repr(p))      # Point2D(x=3, y=4)

    ''' For collections, python uses repr()'''
    l = [Point2D(i, i*2) for i in range(3)]
    print(str(l))       # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4)]
    print(repr(l))      # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4)]
    d = {i: Point2D(i, i*2) for i in range(3)}
    print(str(d))       # {0: Point2D(x=0, y=0), 1: Point2D(x=1, y=2), 2: Point2D(x=2, y=4)}
    print(repr(d))      # {0: Point2D(x=0, y=0), 1: Point2D(x=1, y=2), 2: Point2D(x=2, y=4)}

    ''' format() can give another representation '''
    print('{}'.format(p))
    # "[Formatted point: 3, 4, ]"     instead of     "(3, 4)"
    print('{:r}'.format(p))
    # [Formatted point: 4, 3, r]
    print('{!r}'.format(p))
    # Point2D(x=3, y=4)     <-  uses repr()
    print('{!s}'.format(p))
    # (3, 4)                <-  uses str()

    ''' reprlib: module for other implementations of repr() '''
    import reprlib
    points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
    print(reprlib.repr(points))
    # Instead of printing 1000000 elements, it prints:
    # [Point2D(x=0, y=0), Point2D(x=0, y=1), Point2D(x=0, y=2), Point2D(x=0, y=3), Point2D(x=0, y=4), Point2D(x=0, y=5), ...]
    
    '''ascii(), ord() and chr() '''
    x = 'Hællo'
    y = ascii(x)    
    print(y)        # 'H\xe6llo'
    a = 'æ'
    print(ord(a))   # 230
    print(chr(230)) # æ
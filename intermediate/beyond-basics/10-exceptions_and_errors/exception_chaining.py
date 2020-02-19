import math
import io
import sys

''' Implicit chaining:
        associates chained exception through __context__ atr
'''
class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)
    @property
    def sides(self):
        return self._sides
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)
    def __repr__(self):
        return "TriangleError({!r}, {!r})".format(self.args[0], self._sides)

def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a

def main_implicit():
    try:
        # bug 1: impossible triangle
        a = triangle_area(3, 4, 10)
        print(a)
    except TriangleError as e:
        try:
            # bug 2: write to wrong file (stdin instead of stderr)
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e)                        # 'Illegal triangle' for sides (3, 4, 10)
            print(f)                        # not writable
            print(f.__context__ is e)       # True

'''
    Explicit chaining:
        associates chained exception through __cause__ atr
'''
class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e

def main_explicit():
    # bug 1: call the function with dx=0, causing ZeroDivisionError
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e)                            # Slope cannot be vertical
        print(e.__cause__)                  # division by zero


if __name__ == "__main__":
    main_implicit()
    '''Implicit chaining
        During handling of the above exception, another exception occurred
    '''
    # Traceback (most recent call last):
    # File "exception_chaining.py", line 30, in main
    #     a = triangle_area(3, 4, 10)
    # File "exception_chaining.py", line 22, in triangle_area
    #     raise TriangleError("Illegal triangle", sides)
    # __main__.TriangleError: 'Illegal triangle' for sides (3, 4, 10)

    # During handling of the above exception, another exception occurred:

    # Traceback (most recent call last):
    # File "exception_chaining.py", line 37, in <module>
    #     main()
    # File "exception_chaining.py", line 34, in main
    #     print(e, file=sys.stdin)
    # io.UnsupportedOperation: not writable

    main_explicit()
    '''Explicit chainig
        The above exception was the direct cause of the following exception
    '''
    # Traceback (most recent call last):
    # File "exception_chaining.py", line 55, in main_explicit
    #     inclination(0, 5)
    # File "exception_chaining.py", line 50, in inclination
    #     return math.degrees(math.atan(dy / dx))
    # ZeroDivisionError: division by zero

    # The above exception was the direct cause of the following exception:

    # Traceback (most recent call last):
    # File "exception_chaining.py", line 82, in <module>
    #     main_explicit()
    # File "exception_chaining.py", line 57, in main_explicit
    #     raise InclinationError("Slope cannot be vertical") from e
    # __main__.InclinationError: Slope cannot be vertical
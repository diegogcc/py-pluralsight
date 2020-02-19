''' Create new Exceptions
Example from the area of a triangle'''

import math

class TriangleErrorEmpty(Exception):
    pass

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
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a

def triangle_area_base_error(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleErrorEmpty("Illegal triangle")
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a

def triangle_area_custom_error(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a
    

if __name__ == "__main__":
    # 1
    print(triangle_area(3, 4, 5))           # 6.0
    
    # 2
    try:
        ''' imposible triangle: formula would need to calculate negative roots '''
        t = triangle_area(3, 4, 10)
    except ValueError as e:
        print(repr(e))                      # ValueError('math domain error')

    # 3
    try:
        ''' same impossible triangle but using the function with the handler '''
        t = triangle_area_base_error(3, 4, 10)
    except TriangleErrorEmpty as e:
        print(repr(e))                      # TriangleErrorEmpty('Illegal triangle')

    # 4
    try:
        ''' customize the triangle error '''
        t = triangle_area_custom_error(3, 4, 10)
    except TriangleError as e:
        print(repr(e))                      # TriangleError('Illegal triangle', (3, 4, 10))
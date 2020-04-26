import struct
from pprint import pprint as pp

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue 
    
    def __repr__(self):
        return 'Color({}, {}, {})'.format(self.red, self.green, self.blue)

class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color
    
    def __repr__(self):
        return 'Vertex({}, {})'.format(self.vector, self.color)

def make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z), 
                  Color(red, green, blue))

def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    # Byte order, size and alignment (@ = native order, native size, native alignment)
    # Format characters for the struct module (f = float, H = unsigned short int)
    vertices = []
    for fields in struct.iter_unpack('@3f3Hxx', buffer):
        vertex = make_colored_vertex(*fields)
        vertices.append(vertex)

    pp(vertices)

if __name__ == "__main__":
    main()
    # (3323.176025390625, 6562.23095703125, 9351.2314453125, 3040, 34423, 54321)
    # Values don't match the values in colorpoints.c because:
    # in the original file they are in decimal and the chosen values are not representable in binary
    # also there was a conversion from single-presicion float (on C) to double-presicion float (on Python)
     
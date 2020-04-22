'''
Dispatch on type:
    Function selected base on type of arguments
decorator @singledispatch

Shape classes should only be all about shapeness
    NOT about things that can be done with shapes.
    draw() methods taken out of the classes
'''

class Shape:
    def __init__(self, solid):
        self.solid = solid
    
class Circle(Shape):
    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius 
    
class Parallelogram(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

class Triangle(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb 
        self.pc = pc

def draw_circle(shape):                                       
    print("\u25CF" if shape.solid else "\u25A1")

def draw_parallelogram(shape):                                
    print("\u25B0" if shape.solid else "\u25B1")

def draw_triangle(shape):                                    
    print("\u25B2" if shape.solid else "\u25B3")

''' using isintance '''
# def draw(shape):
#     if isinstance(shape, Circle):
#         draw_circle(shape)
#     elif isinstance(shape, Parallelogram):
#         draw_parallelogram(shape)
#     elif isinstance(shape, Triangle):
#         draw_triangle(shape)
#     else:
#         raise TypeError("Can't draw shape {!r}".format(shape))


''' emulating switch with a type:function dictionary '''
''' this is more fragile because we are doing exact type comparison:
        a subtype of Circle won't work'''
# def draw(shape):
#     drawers = {
#         Circle: draw_circle,
#         Parallelogram: draw_parallelogram,
#         Triangle: draw_triangle,
#     }
#     try:
#         drawer = drawers[type(shape)]
#     except KeyError as e:
#         raise TypeError("Can't draw shape") from e
#     else:
#         drawer(shape)


''' Use singledispatch (from functools) as a way to OVERLOAD the method '''
from functools import singledispatch

@singledispatch
def draw(shape):
    # We first create a GENERIC function that will later be overloaded
    raise TypeError("Don't know how to draw {!r}".format(shape))

@draw.register(Circle)
def _(shape):                                       # As the overload function is associated to the original function
    print("\u25CF" if shape.solid else "\u25A1")    # it doesn't matter what we call them. Thus '_()'

@draw.register(Parallelogram)
def _(shape):                                       # As the overload function is associated to the original function        
    print("\u25B0" if shape.solid else "\u25B1")    # it doesn't matter what we call them. Thus '_()'

@draw.register(Triangle)
def _(shape):                                       # As the overload function is associated to the original function
    print("\u25B2" if shape.solid else "\u25B3")    # it doesn't matter what we call them. Thus '_()'


def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
              Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]
    
    for shape in shapes:
        draw(shape)

if __name__ == "__main__":
    main()
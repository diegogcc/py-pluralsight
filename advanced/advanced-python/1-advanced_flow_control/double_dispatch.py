'''
The @singledispatch decorator should NOT be used on methods (only functions) because:
    singledispatch:
        dispatches ONLY on the type of the FIRST argument (check comment inside method intersects.register(Circle))(25)
        and when methods are called, the first argument will always be 'self'


    Wrong implementation inside class Circle
    Right implementation inside class Parallelogram

Double dispatch:
    shape.intersects(other_shape)
        the function called is selected based on the types of both 'shape' and 'other_shape'
'''
from functools import singledispatch

class Shape:
    def __init__(self, solid):
        self.solid = solid

class Triangle(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb 
        self.pc = pc
    
class Circle(Shape):
    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius 
    
    @singledispatch                     # implementation of a generic method inside the class
    def intersects(self, shape):
        raise TypeError("Don't know how to compute intersection with {!r}".format(shape))

    @intersects.register(Circle)        # can't register the type of the class currently being defined
    def _(self, shape):
        # when calling my_circle.intersects(my_parallelogram), 'my_parallelogram' is actually the 2nd parameter
        # the first being 'my_circle' = self.   

        # self will always be a Circle, an intersects call will ALWAYS dispatch to Circle overload (this overload)
        return circle_intersects_circle(self, shape)

    @intersects.register(Parallelogram)
    def _(self, shape):
        return circle_intersects_parallelogram(self, shape)

    @intersects.register(Triangle)
    def _(self, shape):
        return circle_intersects_triangle(self, shape)

def circle_intersects_circle(circle, shape):
    pass

def circle_intersects_parallelogram(circle, shape):
    pass

def circle_intersects_triangle(circle, shape):
    pass
    
class Parallelogram(Shape):
    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_parallelogram(shape, self)

@singledispatch
def intersects_with_parallelogram(shape, parallelogram):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}"
                    .format(parallelogram, shape))

@intersects_with_parallelogram.register(Circle)
def _(shape, parallelogram):
    return parallelogram_intersects_circle(parallelogram, shape)

@intersects_with_parallelogram.register(Parallelogram)
def _(shape, parallelogram):
    return parallelogram_intersects_parallelogram(parallelogram, shape)

@intersects_with_parallelogram.register(Triangle)
def _(shape, parallelogram):
    return parallelogram_intersects_triangle(parallelogram, shape)

def parallelogram_intersects_circle(parallelogram, shape):
    pass

def parallelogram_intersects_parallelogram(parallelogram, shape):
    pass

def parallelogram_intersects_triangle(parallelogram, shape):
    pass

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
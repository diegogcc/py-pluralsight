'''
Customizing attribute storage 
    not necessarily in __dict__
'''
class Vector:
    
    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                self.__class__, name))

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],                    # slice the _ prefix
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))

class ColoredVector(Vector):

    COLOR_INDEXES = ('red', 'green', 'blue')

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        self.__dict__['color'] = [red, green, blue]
    
    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__['color'][channel]

    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__['color'][channel] = value 

if __name__ == "__main__":
    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)

    print(cv.red)   # 23        ->      Stored in a list at __dict__['color']
    print(cv.p)     # 9         ->      Stored directly in __dict__

    print(dir(cv))
    # ['COLOR_INDEXES', '__class__', ..., '_p', '_q', 'color']


    # super().__repr__ asumes all attribues begin with '_'
    print(cv)   # ColoredVector(p=9, q=14, olor=[23, 44, 238])
    #                                     ^                         Missing 'c' 
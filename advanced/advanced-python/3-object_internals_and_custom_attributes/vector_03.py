'''
Maybe we want to use other references different to x, y
    like u,v 
    like other coordinates system
'''
class Vector:
    
    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],                    # slice the _ prefix
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))

if __name__ == "__main__":
    v = Vector(p=3, q=7)
    print(v)            # Vector(p=3, q=7)

    print(dir(v))
    # ['__class__', '__delattr__', ..., ..., '_p', '_q']

    # attributes 'p' and 'q' are stored in PRIVATE attributes.
    print(v.p)  # AttributeError: 'Vector' object has no attribute 'p'
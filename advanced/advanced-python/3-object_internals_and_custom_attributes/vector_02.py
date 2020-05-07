'''
Maybe we want to use other references different to x, y
    like u,v 
    like other coordinates system
'''
class Vector:
    
    def __init__(self, **coords):
        self.__dict__.update(coords)

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k,
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))

if __name__ == "__main__":
    v = Vector(p=3, q=7)
    print(v)            # Vector(p=3, q=7)

    print(dir(v))
    # ['__class__', '__delattr__', ..., ...,  'p', 'q']

    # attributes 'p' and 'q' are stored in PUBLIC attributes.
    print(v.p)  # 3
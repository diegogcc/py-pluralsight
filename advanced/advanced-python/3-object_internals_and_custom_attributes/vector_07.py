'''
Fake the existence of a private attribute to have read access
before the AttributeError is raised.
We use 
    __getattr__()               -> invoked after requested attribute/property
                                    not found by normal lookup      
        DIFFERENT THAN 
    __getattribute__()          -> invoked instead of normal lookup
'''
class Vector:
    
    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name
        if private_name not in self.__dict__:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                self.__class__, name))
        return getattr(self, private_name)

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

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

    print(v.x)          # AttributeError: <class '__main__.Vector'> object has no attribute 'x'
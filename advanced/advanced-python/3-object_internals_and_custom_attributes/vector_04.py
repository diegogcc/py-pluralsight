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
        print("name =", name)

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

    v.p     # name = p
    v.q     # name = q
    v._p    # 3             -> __getattr__() is not being called when calling an existing attribute
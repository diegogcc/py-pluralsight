'''
    Overriding __getattribute__()
        (invoked INSTEAD of normal attribute lookup)

    __getattribute__(): intercepts all attribute access through the dot '.' operator 
'''

class LoggingProxy:
    """Logs every attribute retreival made against the target objects supplied to the constructor"""
    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name):
        target = super().__getattribute__('target')

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Retreived attribute {!r} = {!r} from {!r}".format(name, value, target))
        return value
    
    def __setattr__(self, name, value):
        target = super().__getattribute__('target')

        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Set attribute {!r} = {!r} on {!r}".format(name, value, target))

if __name__ == "__main__":
    from vector_11 import ColoredVector
    
    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
    cw = LoggingProxy(cv)
    cw.p        # Retreived attribute 'p' = 9 from ColoredVector(23, 44, 238, p=9, q=14)
                # 9
    cw.red      # Retreived attribute 'red' = 23 from ColoredVector(23, 44, 238, p=9, q=14)
                # 23
    
    # Now we can assign to mutable attributes
    cw.red = 55         # Set attribute 'red' = 55 on ColoredVector(55, 44, 238, p=9, q=14)

    # immutable attributes cannot be assigned as expected
    cw.p = 15   # AttributeError: LoggingProxy could not forward request p to ColoredVector(55, 44, 238, p=9, q=14)
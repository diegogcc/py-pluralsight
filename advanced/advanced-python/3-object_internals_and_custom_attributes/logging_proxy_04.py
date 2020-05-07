'''
    Attribute lookup for special methods

    __getattribute__(): only intercepts attribute lookup through the dot operator.

        to solve this the method should be implemented on the proxy.
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
    
    def __repr__(self):
        target = super().__getattribute__('target')
        repr_callable = getattr(target, '__repr__')
        return repr_callable()

if __name__ == "__main__":
    from vector_11 import ColoredVector
    
    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
    cw = LoggingProxy(cv)

    ''' call routed via the proxy and dispatched successfully '''
    cw.__repr__()
    # Retreived attribute '__repr__' = <bound method ColoredVector.__repr__ of ColoredVector(23, 44, 238, p=9, q=14)> from ColoredVector(23, 44, 238, p=9, q=14)
    # 'ColoredVector(23, 44, 238, p=9, q=14)'

    ''' now also proxied '''
    repr(cw)
    # 'ColoredVector(23, 44, 238, p=9, q=14)'
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

if __name__ == "__main__":
    from vector_11 import ColoredVector
    
    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
    cw = LoggingProxy(cv)
    cw.p        # Retreived attribute 'p' = 9 from ColoredVector(23, 44, 238, p=9, q=14)
                # 9
    cw.red      # Retreived attribute 'red' = 23 from ColoredVector(23, 44, 238, p=9, q=14)
                # 23

    ''' Trying to write to an attribute '''
    cw.p = 19           # should be immutable   -> see vector_11.py
    cw.red = 5          # should be mutable     -> see vector_11.py
    
    cw.p        # Retreived attribute 'p' = 9 from ColoredVector(23, 44, 238, p=9, q=14)
                # 9
            # Didn't succeed writing to the attribute
    
    cw.red      # Retreived attribute 'red' = 23 from ColoredVector(23, 44, 238, p=9, q=14)
                # 23
            # Didn't suceed writing to the attribute

    # it didn't succeed because writes through the proxy invoke the inherited object.__setattr__()
    #   which creates new attributes on the logging proxy instances __dict__
    # BUT reads through the proxy are redirected to the target LoggingProxy.__getattribute__
    # this means that the proxy is write only
    # The solution is to override __setattr__ on the proxy (see logging_proxy_02.py)
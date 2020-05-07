'''
    If methods can be accessed by getattr(),
        why don't they appear on a call to __dict__()?

        They are attributes to the class object associated to the instance
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
    from vector_11 import Vector
    
    v = Vector(x=3, y=7)

    v.__dict__
    # {'_x': 3, '_y': 7}

    v.__class__
    # <class 'vector_11.Vector'>        

    v.__class__.__dict__
    # mappingproxy(
    # {'__module__': 'vector_11', '__init__': <function Vector.__init__ at 0x10b67bdd0>, 
    # '__getattr__': <function Vector.__getattr__ at 0x10b67be60>, 
    # '__setattr__': <function Vector.__setattr__ at 0x10b67bef0>, 
    # '__delattr__': <function Vector.__delattr__ at 0x10b67bf80>, 
    # '__repr__': <function Vector.__repr__ at 0x10b6dc050>, 
    # '__dict__': <attribute '__dict__' of 'Vector' objects>, 
    # '__weakref__': <attribute '__weakref__' of 'Vector' objects>, 
    # '__doc__': None}
    # )

    v.__class__.__dict__['__repr__'](v)     # call a method from the dict in class passing instance v as parameter.
    # 'Vector(x=3, y=7)'

    ''' __dict__ inside __class__ is not a normal dict
            is a mappingproxy type
                doesn't support item assignment '''
    v.__class__.__dict__['a_vector_class_attribute'] = 5
    # TypeError: 'mappingproxy' object does not support item assignment

    # to add an attribute to a class you must use setattr function 
    setattr(v.__class__, 'a_vector_class_attribute', 5)
    Vector.a_vector_class_attribute     # 5
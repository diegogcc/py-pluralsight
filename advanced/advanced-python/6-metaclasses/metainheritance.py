"""
                                        7
How does metaclasses interact with inheritance.

For another example of multiple metaclass inheritance see planet.py (the way it uses tracing module)
Planet's metaclass is TracingDescriptorNamingMeta
    which derives from TracingMeta and DescriptorNamingMeta
    both functionalities of the metaclasses still work:
        tracing __prepare__, __new__ and __init__ for the Planet class
        avoiding negative values in the attributes of the Planet instances

If we are having multiple metaclasses there's one advice:
    - use __init__ for configuration (not __new__)
    BECAUSE:        An object can only be allocated once (__new__)
                    but it can be configured multiple times (__init__)
"""
# metaclasses only common because they are both subclass of 'type'
class MetaA(type):
    pass

class MetaB(type):
    pass 

class MetaC(MetaA, MetaB):
    pass

# regular classes that use the metaclasses as their respective subclasses
class A(metaclass=MetaA):
    pass

class B(metaclass=MetaB):
    pass

# class that derives from A 
class D(A):
    pass 

# class that derives from both A and B
# class C(A, B):                                          # produces TypeError: metaclass conflict:
#     pass                                    

class E(A, B, metaclass=MetaC):
    pass

if __name__ == "__main__":
    type(D)
    # <class '__main__.MetaA'>                          <-- metaclasses are inherited
    

    """
    Because of the definition of a class that derives from 2 classes with different metaclasses we get:
    """
    # TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

    """
    We could create a new metaclass MetaC that derives from the other metaclasses MetaA and MetaB.
    And then specify MetaC as the metaclass of the conflicting class 'class E'
    """
    type(E)
    # <class '__main__.MetaC'>


"""
                                        3
    class Widget(metaclass=TracingMeta):
        def action(self, message):
            print(message)
        the_answer = 42

    Widget.metamethod()                     # method defined on the metaclass
    # TracingMeta.metamethod(cls)
    # cls =  <class '__main__.Widget'>  

    w = Widget()
    w.metamethod()                          # not accessible from instance, only from class
    # AttributeError: 'Widget' object has no attribute 'metamethod'


    Overriding __call__ which is a metamethod,
        __call__()                          # in charge of class allocation an initialization
"""

class TracingMeta(type):
    """ we create a custom metaclass.
        it shoould be a subclass of an existing metaclass (type)
    """
    @classmethod                                                    # explicit classmethod (needs decorator)
    def __prepare__(mcs, name, bases, **kwargs):
        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print("  mcs = ", mcs)
        print("  name = ", name)
        print("  bases = ", bases)
        print("  kwargs = ", kwargs)
        namespace = super().__prepare__(name, bases)
        print("<-- namespace = ", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):             # implicit classmethod (doesn't)
        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs = ", mcs)
        print("  name = ", name)
        print("  bases = ", bases)
        print("  namespace = ", namespace)
        print("  kwargs = ", kwargs)
        cls = super().__new__(mcs, name, bases, namespace)
        print("<-- cls = ", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs)")
        print("  cls = ", cls)
        print("  name = ", name)
        print("  bases = ", bases)
        print("  namespace = ", namespace)
        print("  kwargs = ", kwargs)
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls):
        print("TracingMeta.metamethod(cls)")
        print("  cls = ", cls)
        print()

    # other metamethod
    def __call__(cls, *args, **kwargs):
        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print("  cls = ", cls)
        print("  args = ", args)
        print("  kwargs = ", kwargs)
        print("  About to call type.__call__()")
        obj = super().__call__(*args, **kwargs)
        print("  Returned from type.__call__()")
        print("<-- obj = ", obj)
        print()
        return obj 

class TracingClass(metaclass=TracingMeta):
    def __new__(cls, *args, **kwargs):
        print(" TracingClass.__new__(cls, *args, **kwargs)")
        print("   cls = ", cls)
        print("   args = ", args)
        print("   kwargs = ", kwargs)
        obj = super().__new__(cls)
        print(" <-- obj = ", obj)
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print(" TracingClass.__init__(self, *args, **kwargs)")
        print("   self = ", self)
        print("   args = ", args)
        print("   kwargs = ", kwargs)
        print()

# if __name__ == "__main__":
#     # When we import the module, the __prepare__, __new__ and __init__
#     #   are invoked when TracingClass is defined.

#     t = TracingClass(42, keyword="clef")

    # TracingMeta.__call__(cls, *args, **kwargs)                        # invokes __call__ on the metaclass
    # cls =  <class 'tracing02.TracingClass'>
    # args =  (42,)
    # kwargs =  {'keyword': 'clef'}
    # About to call type.__call__()                                     # in charge of class allocation and initialization
    # TracingClass.__new__(cls, *args, **kwargs)
    # cls =  <class 'tracing02.TracingClass'>
    # args =  (42,)
    # kwargs =  {'keyword': 'clef'}
    # <-- obj =  <tracing02.TracingClass object at 0x10d6d7850>

    # TracingClass.__init__(self, *args, **kwargs)
    # self =  <tracing02.TracingClass object at 0x10d6d7850>
    # args =  (42,)
    # kwargs =  {'keyword': 'clef'}

    # Returned from type.__call__()
    # <-- obj =  <tracing02.TracingClass object at 0x10d6d7850>
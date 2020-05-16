"""
                                        1

    class Widget:
        pass

    class Widget(object, metaclass=type):
        pass
    
    'object'    : implicitly the base class
    'type'      : implicitly the metaclass (class of the class)

Writing a class block (inside):
    - Metaclass creates namespace dictionary
    - Python's runtime populates the dictionary reading from the class block.
    - The dictionary is passed to the metaclass
    - The metaclass converts the dictionary into a class object (Widget)
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

if __name__ == "__main__":
    # if we did this from the REPL
    class Widget(metaclass=TracingMeta):
        def action(self, message):
            print(message)
        the_answer = 42
    
    # TracingMeta.__prepare__(name, bases, **kwargs)
    # mcs =  <class 'tracing.TracingMeta'>
    # name =  Widget
    # bases =  ()
    # kwargs =  {}
    # <-- namespace =  {}

    # TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)
    # mcs =  <class 'tracing.TracingMeta'>
    # name =  Widget
    # bases =  ()
    # namespace =  {'__module__': '__main__', '__qualname__': 'Widget', 'action': <function Widget.action at 0x105d678c0>, 'the_answer': 42}
    # kwargs =  {}
    # <-- cls =  <class '__main__.Widget'>

    # TracingMeta.__init__(cls, name, bases, namespace, **kwargs)
    # cls =  <class '__main__.Widget'>
    # name =  Widget
    # bases =  ()
    # namespace =  {'__module__': '__main__', '__qualname__': 'Widget', 'action': <function Widget.action at 0x105d678c0>, 'the_answer': 42}
    # kwargs =  {}

    # Using the metaclass as a class Factory with the kwargs
    class Reticulator(metaclass=TracingMeta, tension=496):
        def reticulate(self, spline):
            print(spline)
        cubic = True 

    # TracingMeta.__prepare__(name, bases, **kwargs)
    # mcs =  <class 'tracing.TracingMeta'>
    # name =  Reticulator
    # bases =  ()
    # kwargs =  {'tension': 496}
    # <-- namespace =  {}

    # TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)
    # mcs =  <class 'tracing.TracingMeta'>
    # name =  Reticulator
    # bases =  ()
    # namespace =  {'__module__': '__main__', '__qualname__': 'Reticulator', 'reticulate': <function Reticulator.reticulate at 0x10a917ef0>, 'cubic': True}
    # kwargs =  {'tension': 496}
    # <-- cls =  <class '__main__.Reticulator'>

    # TracingMeta.__init__(cls, name, bases, namespace, **kwargs)
    # cls =  <class '__main__.Reticulator'>
    # name =  Reticulator
    # bases =  ()
    # namespace =  {'__module__': '__main__', '__qualname__': 'Reticulator', 'reticulate': <function Reticulator.reticulate at 0x10a917ef0>, 'cubic': True}
    # kwargs =  {'tension': 496}
"""
                                        2
    Using the kwargs argument in the metaclass to create a class factory
"""
class EntriesMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("EntriesMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  kwargs = ", kwargs)
        num_entries = kwargs['num_entries']     
        print("  num_entries = ", num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        return cls 

    def __init__(mcs, name, bases, namespace, **kwargs):            # __init__ and __new__ must have the same signature
        pass


if __name__ == "__main__":
    # From the REPL
    class AtoZ(metaclass=EntriesMeta, num_entries=26):
        pass

    # EntriesMeta.__new__(mcs, name, bases, namespace, **kwargs)
    # kwargs =  {'num_entries': 26}
    # num_entries =  26

    # dir(AtoZ)
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
    # '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
    # '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
    # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
    # '__str__', '__subclasshook__', '__weakref__', 
    # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    # 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
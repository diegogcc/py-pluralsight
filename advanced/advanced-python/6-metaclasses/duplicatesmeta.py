"""
                                        5
Creating a metaclass that avoids the creation of classes with duplicate properties like:

    class Dodgy():
        def method(self):
            return "first definition"
        
        def method(self):
            return "second definition"
"""

class OneShotClassNamespace(dict):            # specialized dict
    """ Specializes the ddict behavior and overrides the __init__"""
    def __init__(self, name, existing=None):
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError("Cannot reassign to existing key {!r} of {!r}".format(key, self._name))
        super().__setitem__(key, value)

class ProhibitDuplicatesMeta(type):     # Metaclass that uses the new specialized dictionary

    @classmethod
    def __prepare__(mcs, name, bases):
        return OneShotClassNamespace(name)

if __name__ == "__main__":
    
    # With duplicates

    class Duplicates:
        def method(self):
            return "first definition"
        def method(self):
            return "second definition"
    
    d = Duplicates()
    d.method()          # 'second definition'


    # Without the dupliciates, using the metaclass

    class NoDuplicates(metaclass=ProhibitDuplicatesMeta):
        def method(self):
            return "first definition"
        def method(self):
            return "second definition"
    # TypeError: Cannot reassign to existing key 'method' of 'NoDuplicates'         <- at class definition
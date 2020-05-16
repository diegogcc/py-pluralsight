"""
    Class decorators are another way to modify classes
        class decorators    <   metaclasses
            everything a class decorator can do, a metaclass can also do but not the other way around.
"""
import functools

def invariant(predicate):                   # Decorator Factory
    """Create a class decorator which checks a class invariant.
    Args:
        predicate: A callable to which, after every method invocation,
            the object on which the method was called will be passed.
            The predicate should evaluate to True if the class invariant
            has been maintained, of Ralse if it has been violated.
    Returns:
        A class decorator for checking the class invariant tested by
        the supplied prediciate function.
    """
    def invariant_checking_class_decorator(cls):
        """Aclass decorator for checking invariants."""
        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        return cls
    return invariant_checking_class_decorator

def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(predicate.__doc__, self))
        return result

    setattr(cls, name, invariant_checking_method_decorator)    


def not_below_absolute_zero(temperature):           # used as the predicate
    """Temperature not below absolute zero """
    return temperature._kelvin >= 0


@invariant(not_below_absolute_zero)
class Temperature:
    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return self._kelvin * 9/5 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._kelvin = (value + 459.67) * 5/9

if __name__ == "__main__":
    t = Temperature(5.0)
    # <__main__.Temperature object at 0x100dd0610>
    
    # t = Temperature(-1)
    # RuntimeError: Class invariant 'Temperature not below absolute zero ' violated for <__main__.Temperature object at 0x100e1e0d0>

    """This method has a problem when using properties (like celsius and fahrenheit in Temperature) """
    t.celsius       # -268.15

    t.celsius = -100        # it allows this assignment as expected

    t.celsius = -300        # it allows this assignment BUT IT SHOULD HAVE RAISED THE RuntimeError.

    # Only when we call t.get_kelvin() the error is raised
    # This happens because the properties are declared with descriptors that wrap the methods.
    #   those descriptors are not callable and escape the logic of the decorator 
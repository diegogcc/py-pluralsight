"""
    Demonstration that we can chain class decorators just as we can with function decorators
        using a hypotetical value absolute_hot
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
        
        # we have to look for proper objects
        property_names = [name for name, attr in vars(cls).items() if isinstance(attr, property)]
        for name in property_names:
            _wrap_property_with_invariant_checking_proxy(cls, name, predicate)

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


def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
    prop = getattr(cls, name)
    assert isinstance(prop, property)

    invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)

    setattr(cls, name, invariant_checking_proxy)


class InvariantCheckingPropertyProxy:
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def __get__(self, instance, owner):
        if instance is None:
            return self._referent
        result = self._referent.__get__(instance, owner)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result

    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result

    def __delete__(self, instance):
        result = self._referent.__delete__(instance)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result
            

def not_below_absolute_zero(temperature):           # used as the predicate
    """Temperature not below absolute zero """
    return temperature._kelvin >= 0


def below_absolte_hot(temperature):                 # used as second decorator
    """Temperature below absolute hot"""
    return temperature._kelvin <= 1.416785e32


@invariant(below_absolte_hot)
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

    # not_below_absolute_zero   decorator working
    t.set_kelvin(-300)
    # RuntimeError: Class invariant 'Temperature not below absolute zero'

    # below_absolute_hot        decorator also working
    t.set_kelvin(1e33)
    # RuntimeError: Class invariant 'Temperature below absolute hot'

    """ issue with this implementation:
            for class properties (e.g celsius) the below limit decorator works 
            but not the new top limit.

            We see how to solve this with the  ABSTRACT BASE CLASS chapter (class_decorators004.py).
    """
    t.celsius = -300
    # RuntimeError: Class invariant 'Temperature not below absolute zero '

    t.celsius = 1e34    # Not detected
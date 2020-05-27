"""
    The implementation of class_decorators03.py was only catching the innermost decorator
    This is because in the definition of 'invariant', we detect specifically 'property' instances
        We create PropertyDataDescriptor as an abstract descriptor,
        its subclasses are 'property' (virtual) and 'InvariantCheckingPropertyProxy' (real)
        And we change 'invariant' check to use this new decorator
"""
from abc import ABC, abstractmethod
import functools


# Decorator Factory
def invariant(predicate):                   
    """Create a class decorator which checks a class invariant.

    Args:
        predicate: A callable to which, after every method invocation,
            the object on which the method was called will be passed.
            The predicate should evaluate to True if the class invariant
            has been maintained, or False if it has been violated.

    Returns:
        A class decorator for checking the class invariant tested by
        the supplied predicate function.
    """
    def invariant_checking_class_decorator(cls):
        """A class decorator for checking invariants."""
        
        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        
        # we have to look for proper objects
        property_names = [name for name, attr in vars(cls).items() if isinstance(attr, PropertyDataDescriptor)]
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
    pass


# Abstract base class for a Decorator
class PropertyDataDescriptor(ABC):              
    
    @abstractmethod
    def __get__(self, instance, owner):
        raise NotImplementedError

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError

    @abstractmethod
    def __delete__(self, instance):
        raise NotImplementedError

    @property
    @abstractmethod
    def __isabstractmethod__(self):
        raise NotImplementedError

# 'property' as a virtual subclass
PropertyDataDescriptor.register(property)       

# this descriptor as a real subclass 
class InvariantCheckingPropertyProxy(PropertyDataDescriptor):       
    
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def __get__(self, instance, owner):
        if instance is None:
            return self
        result = self._referent.__get__(instance, owner)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
        return result

    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
        return result

    def __delete__(self, instance):
        result = self._referent.__delete__(instance)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
        return result

    # we override this  method
    def __isabstractmethod__(self):                  
        return self._referent.__isabstractmethod__
    

def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
    prop = getattr(cls, name)

    invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)
    setattr(cls, name, invariant_checking_proxy)

# used as the predicate
def not_below_absolute_zero(temperature):           
    """Temperature not below absolute zero"""
    return temperature._kelvin >= 0


# used as second decorator
def below_absolute_hot(temperature):                 
    """Temperature below absolute hot"""
    return temperature._kelvin <= 1.416785e32


@invariant(below_absolute_hot)
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

    """ 
    Now both wrappers work
    """
    t.celsius = -300
    # RuntimeError: Class invariant 'Temperature not below absolute zero'      
    t.celsius = 1e34
    # RuntimeError: Class invariant 'Temperature below absolute hot'
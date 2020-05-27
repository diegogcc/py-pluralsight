"""
Implementing abstract base classes using the standard library abc
    abc module
        - ABCMeta metaclass
        - ABC base class
        - @abstracmethod decorator
            can also be combined with other decorators (@staticimethod, @classmethod and @property) 
            as long as @abstractmethod is the innermost one.

                class AbstractBaseClass(ABC):
                    @staticmethod
                    @abstractmethod
                    def an_abstract_static_method():
                        raise NotImplementedError
Declase abstract methods:
    abstract method: a method which is declared bt which doesn't have a useful definition
        must be overridden in concrete classes

For @properties: they are implemented using descriptors.
For own descriptor implementations: 
    The descriptor should identify as abstract by implementing __isabstractmethod__()

    class MyDataDescriptor(ABC):
        @abstractmethod
        def __get__(self, instance, owner):
            pass
        @abstractmethod
        def __set__(self, instance, value):
            pass
        @abstractmethod
        def __delete__(self, instance):
            pass
        @property
        def __isabstractmethod__(self):
            return True # or False if not abstract

Example:
    class AbstractBaseClass(ABC):
        @property
        @abstractmethod
        def abstract_property(self):
            raise NotImplementedError
        
        @property
        def concrete_property(self):
            return "sand, cement, water"
    AbstractBaseClass.abstract_property.__isabstractmethod__        # True
    AbstractBaseClass.concrete_property.__isabstractmethod__        # False
"""
from abc import ABC, abstractmethod

class Sword(ABC):       # virtual base class 
    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'parry') and callable(sub.parry)
                and
                hasattr(sub, 'thrust') and callable(sub.thrust)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)

    @abstractmethod
    def swipe(self):
        raise NotImplementedError       # must be overridden in concrete class

    @abstractmethod
    def parry(self):
        raise NotImplementedError       # must be overridden in concrete class

    @abstractmethod
    def thrust(self):
        print("Thrusting...")


class BroadSword(Sword):
    def swipe(self):
        print("Swoosh!")
    
    def sharpen(self):
        print("Shink!")

class BroadSword2(Sword):
    def swipe(self):
        print("Swoosh!")
    
    def thrust(self):
        super().thrust()       

    def parry(self):
        print("Parry")
    
    def sharpen(self):
        print("Shink!")

class SamuraiSword:
    def swipe(self):
        print("Slice!")
    
    def sharpen(self):
        print("Shink!")

class Rifle:
    def fire(self):
        print("Bang!")

if __name__ == "__main__":
    """ If we now make BroadSword an explicit subclass of Sword, 
    we won't be able to instantiate it because we haven't implemented parry and thrust"""
    # broad_sword = BroadSword()      # TypeError: Can't instantiate abstract class BroadSword with abstract methods parry, thrust


    """ We have to implement those methods in the concrete class (see BroadSword2) """
    broad_sword = BroadSword2()

    """ The requirement of implementation of abstractmethods only applies for explicit subclasses.
    For SamuraiSword, it's not necessary to implement parry() and thrust() """
    samurai_sword = SamuraiSword()
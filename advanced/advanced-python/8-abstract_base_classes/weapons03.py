"""
Implementing abstract base classes using the standard library abc
    abc module
        - ABCMeta metaclass
            1. implements __subclasscheck__() and __instancecheck__() -> delegate to:
            __subclasshook__()
                returns True, False or NotImplemented 
                
            2. register a class as a virtual subclass with an abstract base class
                class Text(metaclass=ABCMeta):
                    pass
                Text.register(str)          # returns the class it registers
                issubclass(str, Text)       # True
                isinstance("Hello", Text)   # True

                @Text.register
                class Prose:
                    pass
                issubclass(Prose, Text)     # True
        - ABC base class
            A class named 'ABC' that has 'ABCMeta' as its metaclass.
            making it easier to declare abstract base classes (see Sword2)
        - @abstracmethod decorator
"""
from abc import ABC, ABCMeta

class Sword(metaclass=ABCMeta):       # virtual base class 
    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)

    def thrust(self):
        print("Thrusting...")

class Sword2(ABC):
    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)

    def thrust(self):
        print("Thrusting...")

class BroadSword:
    def swipe(self):
        print("Swoosh!")
    
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

@Sword.register
class LightSaber:
    def swipe(self):
        print("Ffffkrrrshhzwooom.woom..woom")

if __name__ == "__main__":
    issubclass(SamuraiSword, Sword)     # True
    issubclass(Rifle, Sword)            # False
    
    broad_sword = BroadSword()
    isinstance(broad_sword, Sword)      # True

    """ Class Lightsaber registered as a subclass of Sword, but it doesn't implement the sharpen method"""
    issubclass(LightSaber, Sword)       # True

    """ Using the regular class ABC we can also declare the abstract base class """
    issubclass(SamuraiSword, Sword2)    # True
    issubclass(LightSaber, Sword2)      # False
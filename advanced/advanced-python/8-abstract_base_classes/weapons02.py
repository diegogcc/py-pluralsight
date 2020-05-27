"""
Implementation of __instancecheck__

Non-transitive Subclass Relationships:
    
    - If A is subclass of B, B isn't necessarily superclass of A.
    
    - If A is subclass of B, and B is subclass of C:
        A isn't necessarily a subclass of C.
"""

class SwordMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))

class Sword(metaclass=SwordMeta):       # virtual base class   
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

if __name__ == "__main__":

    """Unlike regular base classes, virtual base classes don't play a role on method resolution"""
    broad_sword = BroadSword()
    isinstance(broad_sword, Sword)  # True
    broad_sword.swipe()             # Swoosh!

    """ We have problems invoking thrust()"""
    broad_sword.thrust()            # AttributeError: 'BroadSword' object has no attribute 'thrust'

    """ If we look into the BroadSword __mro__ (method resolution order) we see that Sword is not there"""
    BroadSword.__mro__              # (<class '__main__.BroadSword'>, <class 'object'>)     <- no 'Sword'

    """ For this reason it is not possible to call virtual base classes using super() """
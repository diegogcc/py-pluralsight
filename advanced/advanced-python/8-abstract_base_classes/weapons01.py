"""
ABSTRACT BASE CLASS  
    Base because is the target of he inheritance
    Abstract because cannot be instantiated on its own (only as part of a derived type which is concrete)

    ABCs:   
        SPECIFICATION:  effective for specifying interface protocols 
        DETECTION:      can be used to detect conforming objects

    VIRTUAL BASE CLASS:     can be considered a subclass of the ABC without explicitly inheriting from it.
"""

class SwordMeta(type):
    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))

class Sword(metaclass=SwordMeta):       # virtual base class
    pass

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

    """ BroadSword and SamuariSword are subclasses of Sword even though there's no explicit 
        relationship through inheritance """

    issubclass(BroadSword, Sword)       # True
    issubclass(SamuraiSword, Sword)     # True
    issubclass(Rifle, Sword)            # False

    """ Although, inconsistent results will be found using isinstance 
        because we haven't implemented __instancecheck__ """

    samurai_sword = SamuraiSword()
    isinstance(samurai_sword, Sword)    # False
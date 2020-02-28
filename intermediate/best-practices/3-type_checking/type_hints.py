'''
TYPE HINTS:
    Make python statically typed
    
    find type hints in GREEN

'''

__author__ = "Diego Campo"
import random
from abc import ABC, abstractmethod
from typing import Tuple

"""
    weapons.py
    ----------

    This module contains classes for Weapons.
"""


class Weapon(ABC):
    """This abstract class defines the method :meth:`attack` that should be implemented
    by subclasses.
    """

    @abstractmethod
    def attack(self, other) -> Tuple[int, str]:     # TYPE HINT
        """This method should return a tuple (damage, text): how much damage was dealt
        and what text to output. Text is a format string with placeholders for attacker
        and defender.
        """


class Sword(Weapon):
    """A primitive close-range weapon. It deals either 5 or 10 damage with a 50/50 chance.
    """

    def attack(self) -> Tuple[int, str]:            # TYPE HINT
        return (random.choice([10, 15]), random.choice(["Bam!", "Whack!", "Pow!"]))


class FireBreath(Weapon):
    """FireBreath is a weapon only wielded by dragons or wizards. It can deal a lot of damage,
    but it also has its drawbacks. There is a 30% chance that the attack will not work, and after
    a successful attack you will need to wait a while before you will be able to breath fire again.
    """

    def __init__(self) -> None:                     # TYPE HINT 
        ''' The number of attacks we will have to wait until we can fire again'''
        self._cooldown: int = 0

    def attack(self) -> Tuple[int, str]:
        if self._cooldown <= 0:
            dmg: int                                # TYPE HINT
            sound: str                              # TYPE HINT
            dmg = random.choice([0, 40])
            if dmg > 0:
                self._cooldown = 2
                sound = "Boom! Dragon Fire!"
            else:
                sound = "The dragon produces only smoke.."
            return dmg, sound
        else:
            self._cooldown -= 1
            return 0, "(waiting until it can breath fire again)"


"""
    player.py
    ---------

    This module contains the Player class that represents game characters.
"""


class Player:
    """
    The Player class represents the characters in the game.

    :ivar health: The current health of the character. Starts at 100.
                  Once it reaches 0, we're dead.
    """

    # TYPE HINTS:
    # Add the expected value for the params
    def __init__(self, name: str, weapon: Weapon, health: int):
        """
        Create a new Player.

        :param name: The name of the Player.
        :param weapon: The weapon that this Player uses to fight with.
        """
        self.name = name
        self.weapon = weapon
        self.health = 100

    # TYPE HINTS:
    # Add the return value of the method
    def take_hit(self, damage:int) -> int:
        self.health -= damage
        return self.health

    @property
    def is_alive(self) -> bool:
        """True if :attr:`health` is larger than 0, False otherwise"""
        return self.health > 0

    def __str__(self) -> str:
        return "Player {} has {} health and brings his {} to the fight".format(
            self.name, self.health, type(self.weapon).__name__
        )

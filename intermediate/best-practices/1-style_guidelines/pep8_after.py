'''
In VSCode run command 'autopep8'

pylint:
    run from the command line:
        '$ pylint file_name.py'
        '$ pylint module/'
    create rcfile:
        '$ pylint --generate-rcfile > pylintrc'


pycodestyle:
    (flags only pep8 style errors/warnings)
    run from the command line:
        '$ pycodestyle file_name.py'
        '$ pycodestyle module/'


black:
    (makes the changes when you call it)
    run from the command line:
        '$ black file_name.py'
        '$ black module/'
'''

__author__ = "Reindert-Jan Ekker"

import random

from lib.weapons import Sword, FireBreath
from lib.player import Player


class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def run(self):
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.attack()
            print(attacker.name, "attacks:", sound)
            print(attacker.name, "did", dmg, "damage")
            defender.take_hit(dmg)
        print(attacker.name, "won with",
              attacker.health, "health left")


if __name__ == "__main__":
    random.seed()
    g = Game(
        Player("The Knight", Sword()),
        Player("The Dragon", FireBreath())
    )
    g.run()

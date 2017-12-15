import random
from item import Weapon, Potion


class Creature:
    def __init__(self, name, species, is_player=False):
        self.name = name
        self.species = species
        self.max_health = self.set_health()
        self.health = self.max_health
        self.weapon = self.starting_weapon()
        self.inventory = []
        self.is_player = is_player

    @staticmethod
    def set_health():
        return random.randint(30,50)

    @staticmethod
    def starting_weapon():
        return Weapon()

    def drop_weapon(self):
        self.weapon = None

    def equip_weapon(self, found_weapon):
        self.weapon = found_weapon

    def store_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        return '\n'.join([x.name for x in self.inventory])

    def drink_potion(self,potion):
        if self.health == self.max_health:
            return 'Your hp is already at maximum. You have {} hp.'.format(self.health)
        elif self.health + potion.health_restored >= self.max_health:
            self.health = self.max_health
            return 'You have been healed! Your hp have been fully restored. You now have {} hp.'.format(self.health)
        else:
            self.health += potion.health_restored
            return 'You have been healed for {} hp! You now have {} hp.'.format(potion.health_restored, self.health)

    def describe(self):
        if self.weapon:
            return 'a {} named {} with {} health points, armed with {}'.format(self.species, self.name, self.health, self.weapon.describe())
        else:
            return 'a {} named {} with {} health points, unarmed'.format(self.species, self.name, self.health)

if __name__ == '__main__':
    donna = Creature('Donna', 'human')
    larry = Creature('Larry', 'centaur')
    print(donna.describe())
    print(larry.describe())

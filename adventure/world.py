from creature import Creature
from item import Weapon, Potion


class Room:
    def __init__(self, door, info_text):
        self.exit = door
        self.items = []
        self.creatures = []
        self.info_text = info_text

    def inspect_items(self):
        return ', '.join(x.name for x in self.items)

    def inspect_creatures(self):
        return ', '.join(['a ' + x.species for x in self.creatures if not x.is_player])

    def describe(self):
        return 'You are standing in {}. {}.'.format(self.info_text, self.exit)


if __name__ == '__main__':
    start = Room('a door', 'a dark room')
    player = Creature('Li', 'human')
    monster = Creature('Klarg', 'hugbear')
    p = Potion()
    w = Weapon()
    start.creatures.append(player)
    start.creatures.append(monster)
    start.items.append(p)
    start.items.append(w)
    print(start.describe())
    print(start.inspect_creatures())
    print(start.inspect_items())

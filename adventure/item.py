import random


class Weapon:
    def __init__(self):
        self.location = None
        self.damage = self.starting_damage()
        self.weapon_type = self.select_weapon()
        self.adjective = self.set_adjective()
        self.name = self.get_name()

    @staticmethod
    def starting_damage():
        return random.randint(3, 12)

    @staticmethod
    def select_weapon():
        starter_weapons = ['sling', 'stick', 'dagger']
        return random.choice(starter_weapons)

    @staticmethod
    def set_adjective():
        adj_list = ['ugly', 'old', 'dusty', 'large', 'small', 'sturdy']
        adj = random.choice(adj_list)
        return adj

    def describe(self):
        if self.adjective[0] in 'aeiou':
            return 'an {} that does {} damage'.format(self.name,self.damage)
        else:
            return 'a {} that does {} damage'.format(self.name,self.damage)

    def get_name(self):
        if self.adjective[0] in 'aeiou':
            return 'an {} {}'.format(self.adjective,self.weapon_type)
        else:
            return 'a {} {}'.format(self.adjective,self.weapon_type)


class Potion:
    def __init__(self):
        self.location = None
        self.health_restored = self.potion_strength()
        self.adjective = self.set_adjective()
        self.color = self.set_color()
        self.name = 'a {} {} potion'.format(self.adjective,self.color)

    def set_adjective(self):
        adj_list = ['cloudy', 'murky', 'glowing', 'swirling']
        return random.choice(adj_list)

    def set_color(self):
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'black', 'pink']
        return random.choice(color_list)

    def potion_strength(self):
        return random.randint(10,20)

    def describe(self):
        return 'a {} {} potion that will heal {} points of damage'.format(self.adjective, self.color, self.health_restored)


if __name__ == '__main__':
    player_weapon = Weapon()
    print(player_weapon.describe())
    p = Potion()
    print(p.describe())

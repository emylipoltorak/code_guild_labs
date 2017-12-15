from creature import Creature
from item import Potion
from world import Room
from time import sleep

def teatime_with_klarg():
    ext = Room('Before you is a heavy stone gate', 'a large, open field, facing a stone wall')
    first_chamber = Room('There is a trap door in the floor',
                         'a massive stone walled chamber. There is dust on the walls, and the room is lit by an extravagant but tattered chandelier')
    second_chamber = Room('In the middle of the room sits a glittering gold chest', 'a small dirt room')
    chest = Room('', 'In the golden chest, you find: ')
    p_name = input('What is your name? ')
    p_species = input('What type of creature are you? ')
    player = Creature(p_name, p_species, is_player=True)
    ext.creatures.append(player)
    klarg = Creature('Klarg', 'Hugbear')
    first_chamber.creatures.append(klarg)
    pot = Potion()
    chest.items.append(pot)

    print(ext.describe())
    sleep(2)
    print('You are {}.'.format(player.describe()))
    sleep(2.5)
    while True:
        if player.weapon:
            choice = input('What would you like to do? O for open gate, Q for quit, D for drop weapon. ').upper()
        else:
            choice = input('What would you like to do? O for open gate, Q for quit. ').upper()
        if choice == 'O':
            break
        elif choice == 'D':
            ext.items.append(player.weapon)
            player.drop_weapon()
            print('You are unarmed.')
            sleep(1.5)
            print('On the ground, you see {}'.format(ext.items[0].describe()))
            sleep(1.5)
            choice = input( 'Enter I to put the weapon in your inventory, E to equip it, or L to leave it on the ground: ').upper()
            if choice == 'I':
                player.store_item(ext.items[0])
            elif choice == 'E':
                player.equip_weapon(ext.items[0])
                sleep(1.5)
                print('You are armed with {}.'.format(player.weapon.name))
            elif choice == 'L':
                pass
            continue
        elif choice == 'Q':
            print('Goodbye!')
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue
    print(first_chamber.describe())
    sleep(3)
    ext.creatures.remove(player)
    first_chamber.creatures.append(player)
    print('In the room you see {}.'.format(first_chamber.inspect_creatures()))
    sleep(1.5)
    print('The {} says "Hello, my name is {}!"'.format(klarg.species, klarg.name))
    sleep(1.5)
    print('{}: Welcome to my home! Would you like some tea?'.format(klarg.name))
    sleep(1.5)
    while True:
        choice = input('Enter Y for yes or N for no thank you: ').upper()
        if choice == 'Y':
            print('{}: I have sleepytime. Let me get you some.'.format(klarg.name))
            sleep(1.5)
            print('You and {} the {} have a nice cup of tea together.'.format(klarg.name, klarg.species))
            break
        elif choice == 'N':
            print('{}: You come into my house, looking for my treasure, I assume, and you won\'t even sit and drink a cup of tea with me?'.format(klarg.name))
            sleep(2.5)
            print('{} looks offended.'.format(klarg.name))
            sleep(1.5)
            print('{}: Please leave.'.format(klarg.name))
            sleep(1.5)
            print('{} escorts you out. You have lost the game and will not get the treasure.'.format(klarg.name))
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue
    sleep(1.5)
    print('{}: I assume you\'re here for the treasure? '.format(klarg.name))
    sleep(1.5)
    while True:
        choice = input('Enter Y for yes or N for no: ').upper()
        if choice == 'Y':
            print('{}: Right this way.'.format(klarg.name))
            sleep(1.5)
            print('{} opens the trap door.'.format(klarg.name))
            break
        elif choice == 'N':
            print('You and {} have another cup of tea, then you go home. You didn\'t get the treasure, but you made a new friend.'.format(klarg.name))
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue
    sleep(1)
    while True:
        choice = input('Enter D to go down into the trap door, or S to stay up here: ').upper()
        if choice == 'D':
            first_chamber.creatures.remove(player)
            first_chamber.creatures.remove(klarg)
            second_chamber.creatures.append(player)
            second_chamber.creatures.append(klarg)
            print(second_chamber.describe())
            break
        elif choice == 'S':
            sleep(2.5)
            print('{} closes the trap door.'.format(klarg.name))
            sleep(1.5)
            print('{}: You changed your mind? Ok!'.format(klarg.name))
            sleep(1.5)
            print('You and {} have another cup of tea, then you go home. You didn\'t get the treasure, but you made a new friend.'.format(klarg.name))
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue
    sleep(1.5)
    while True:
        choice = input('Enter O to open the chest, or L to leave: ').upper()
        if choice == 'O':
            print(chest.info_text)
            sleep(1.5)
            print('...')
            sleep(.7)
            print('...')
            sleep(.7)
            print(chest.items[0].name)
            break
        elif choice == 'L':
            print('{}: You changed your mind? Ok!'.format(klarg.name))
            sleep(1.5)
            print('You and {} have another cup of tea, then you go home. You didn\'t get the treasure, but you made a new friend.'.format(klarg.name))
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue
    sleep(1)
    while True:
        choice = input('Enter I to put the potion in your inventory, D to drink the potion, or L to leave: ').upper()
        if choice == 'L':
            print('{}: You changed your mind? Ok!'.format(klarg.name))
            sleep(1.5)
            print('You and {} have another cup of tea, then you go home. You didn\'t get the treasure, but you made a new friend.'.format(klarg.name))
            sleep(1.5)
            exit()
        elif choice == 'D':
            sleep(1.5)
            print(player.drink_potion(chest.items[0]))
            sleep(1.5)
            print('You have won the game. Congratulations!')
            sleep(1.5)
            exit()
        elif choice == 'I':
            print('You got {}!'.format(chest.items[0].name))
            player.store_item(chest.items.pop())
            sleep(1.5)
            print('Your inventory: {}'.format(player.show_inventory()))
            sleep(1.5)
            print('You have won the game. Congratulations!')
            sleep(1.5)
            exit()
        else:
            print('That wasn\'t a valid entry.')
            continue

if __name__ == '__main__':
    teatime_with_klarg()


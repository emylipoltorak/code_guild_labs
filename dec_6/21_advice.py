"""
>>> advise_player('A', 'K')
'21 Blackjack!'
>>> advise_player(10, 5)
'15 Hit.'
>>> advise_player('Q', 5)
'15 Hit.'
>>> advise_player('J', 'K')
'20 Stay.'
>>> advise_player(10, 5, 'J')
'25 You lost.'
>>> advise_player()
Traceback (most recent call last):
    ...
ValueError: Requires at least 2 arguments.
>>> advise_player('Q',3,'A')
'14 Hit.'
"""

def advise_player(*args):
    total = 0
    if len(args) < 2:
        raise ValueError('Requires at least 2 arguments.')
    for a in args:
        if type(a) == str and a.upper() in 'JQK':
            total += 10
        elif type(a)==int:
            total += a
        elif type(a) == str and a.upper() == 'A':
            if total + 11 <= 21:
                total += 11
            else:
                total += 1


    if len(args) == 2 and total == 21:
        return "21 Blackjack!"
    elif total > 21:
        return "{} You lost.".format(total)
    else :
        return "{} Stay.".format(total) if total > 15 else "{} Hit.".format(total)

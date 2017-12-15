import math

def guess(n):
    return input('Is your number {}? Tell me "yes", "higher", or "lower". '.format(n)).lower()

def binary_search(count=0,top=4000000000, bottom=0):
    n = bottom+math.ceil((top-bottom)/2)
    attempt = guess(n)
    if attempt in 'yes':
        count +=1
        return 'Your number was {}. It took me {} tries to guess your number.'.format(n,count)
    elif attempt in "lower":
        return binary_search(count+1,top=n, bottom=bottom)
    else:
        return binary_search(count+1,top=top,bottom=n)

def set_difficulty():
    difficulty = int(input('Select a difficulty between 1 and 5: '))
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 300
    elif difficulty == 3:
        return 1000000
    elif difficulty == 4:
        return 500000000
    elif difficulty == 5:
        return 4000000000000

def guess_the_number():
    start = input('Would you like to play a game? Enter y/n: ').lower()
    if start in 'yes':
        difficulty = set_difficulty()
        input('Pick a number between 1 and {}. When you\'re ready, press enter: '.format(difficulty) )
        print(binary_search(top=difficulty))
    else:
        return 'Ok, maybe another time.'
    again = input('Would you like to play again? y/n: ').lower()
    while again in 'yes':
        difficulty = set_difficulty()
        input('Pick a number between 1 and {}. When you\'re ready, press enter: '.format(difficulty) )
        binary_search(top=difficulty)
        again = input('Would you like to play again? y/n: ')
    return 'Goodbye.'

print(guess_the_number())

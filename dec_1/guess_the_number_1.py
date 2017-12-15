from random import randint
import time

def evaluate_guess(guess,n):
    if guess == n:
        return 'You got it! My number was {}'.format(guess)
    elif guess < n:
        return 'My number is higher than {}. Guess again! '.format(guess)
    else:
        return 'My number is lower than {}. Guess again! '.format(guess)

def define_upper():
    difficulty = int(input('Select a difficulty between 1 and 5: '))
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 100
    elif difficulty == 3:
        return 1000
    elif difficulty == 4:
        return 100000
    elif difficulty == 5:
        return 100000000

def guess_the_number(upper=10):
    n = randint(1,upper)
    guess = int(input('My number is between 1 and {}. What is your guess? '.format(upper)))
    time.sleep(.5)
    guess_counter = 1
    while guess != n:
        print(evaluate_guess(guess, n))
        guess = int(input('What is your guess? '))
        time.sleep(.5)
        guess_counter+=1
    return '{}. You took {} tries to guess my number.'.format(evaluate_guess(guess,n),guess_counter)

def user_interface():
    while True:
        print(guess_the_number(define_upper()))
        again = input('Would you like to play again? y/n ').lower()
        if not again in 'yes':
            return 'I hope you enjoyed this game. Have a nice day!'

print(user_interface())

def fizz_buzz(n):
    for x in range(1,n+1):
        msg = ''
        if not x % 3:
            msg += 'Fizz'
        if not x % 5:
            msg += 'Buzz'
        print(msg or x)

if __name__ == '__main__':
    try:
        n = int(input('Enter a number: '))
    except TypeError:
        print('That wasn\'t a number.')
    fizz_buzz(n)

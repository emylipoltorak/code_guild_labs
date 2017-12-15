import datetime

name = input('What is your name?: ')
year = input('What year (YYYY) were you born?: ')
age = datetime.datetime.now().year - int(year)
greet = 'Hello, {n}. You are {cat} years old.'.format(n=name, cat=age)

print(greet)

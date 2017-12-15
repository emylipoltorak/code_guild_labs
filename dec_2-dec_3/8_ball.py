import random
import time

def magic_8_ball():
    answers = ['It is certain', 'It is decidedly so','Without a doubt',
    'Yes definitely','You may rely on it','As I see it, yes','Most likely',
    'Outlook good','Yes','Signs point to yes','Reply hazy try again',
    'Ask again later','Better not tell you now','Cannot predict now',
    'Concentrate and ask again','Don\'t count on it','My reply is no',
    'My sources say no','Outlook not so good','Very doubtful']
    return random.choice(answers)

def make_prediction():
    input('The medium is ready to hear your question. \nWhat question do you have for the medium? ')
    time.sleep(.500)
    print('The medium has entered into contemplation.')
    time.sleep(1)
    for x in range(random.randint(2,5)):
        print('*'*42)
        time.sleep(1)
    print('The medium is ready with her answer.')
    time.sleep(1)
    return 'The medium says "{}".'.format(magic_8_ball())

def user_interface(question_count=0):
    if not question_count:
        print('**~~~Hello~~~**' )
        time.sleep(.500)
        print(make_prediction())
        return user_interface(question_count+1)
    else:
        again = input('Do you have another question for the medium? y/n: ').lower()
        if again in 'no':
            return 'The medium has enjoyed speaking with you. Please take her advice to heart.'
        else:
            print(make_prediction())
            return user_interface(question_count+1)

print(user_interface())

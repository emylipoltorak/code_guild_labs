import string
vowels = 'aeiouyAEIOUY'
again = 0

def pig_latin():
    word = input('What is your word?: ')
    end = ''
    if word[-1] in string.punctuation:
        end = word[-1]
        word = word[:len(word)-1]
    if word[0] in vowels and word[0] not in 'Yy':
        output = word+'yay'
    else:
        first_vowel = 0
        for index, char in enumerate(word):
            if char in vowels:
                first_vowel = index
                break
        output = word[first_vowel:]+word[:first_vowel]+'ay'
    if word[0] == word[0].upper():
        output = output.title()
    return '{} in pig latin is {}'.format(word,output+end)

def pig_repeater():
    global again
    if not again:
        translate = input('Would you like to translate a word into pig latin? y/n: ')
        if translate.lower() in 'yes':
            again += 1
            print(pig_latin())
            return pig_repeater()
        else:
            return 'Goodbye!'
    else:
        translate = input('Would you like to translate another word? y/n: : ')
        if translate.lower() in 'yes':
            again += 1
            print(pig_latin())
            return pig_repeater()
        else:
            return 'You have translated {} words. Goodbye!'.format(again)


print(pig_repeater())

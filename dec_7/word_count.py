from pathlib import Path
import datetime

def word_frequency(text_file, less_common = False):
    most_common = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day',
    'do','even','find','first','for','from','get','give','go','have','he','her','here','him','his','how','i','if',
    'in','into','it','its','just','know','like','look','make','man','many','me','more','my','new','no','not','now',
    'of','on','one','only','or','other','our','out','people','say','see','she','so','some','take','tell','than',
    'that','the','their','them','then','there','these','they','thing','think','this','those','time','to','two',
    'up','use','very','want','way','we','well','what','when','which','who','will','with','would','year','you','your']
    freq_dict = {}
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.replace('-',' ').split():
                word = ''.join(e for e in word if e.isalpha()).lower()
                try:
                    if word:
                        freq_dict[word]['count']+=1
                except KeyError:
                    if word:
                        freq_dict[word]={}
                        freq_dict[word]['count']=1
    if less_common:
        for item in most_common:
            try:
                del freq_dict[item]
            except KeyError:
                pass
    return freq_dict

def words(text_file):
    for line in text_file:
        for word in line.split():
            yield ''.join(e for e in word if e.isalpha())

def most_common(lst):
    return max(set(lst), key=lst.count)

def bi_gram(text_file,dictionary,query):
    with open(text_file, 'r') as f:
        word_generator = words(f)
        next_words = []
        for word in word_generator:
            if word == query:
                next_words.append(next(word_generator))
    return most_common(next_words)


def user_interface():
    while True:
        text_file = Path(input('What file would you like to analyze? '))
        try:
            text_file.resolve()
        except FileNotFoundError:
            print('Sorry, file not found.')
            continue
        analysis_type = input('What analysis would you like to do? Enter BG for bi-gram or TMC for the ten most common words: ').lower()
        if analysis_type in 'tmc':
            exclude = input('Would you like to exclude the 100 most common words? y/n: ').lower()
            if exclude in 'yes':
                freq_dict = word_frequency(text_file,less_common=True)
            else:
                freq_dict = word_frequency(text_file)
            top_10 = sorted(freq_dict, key=lambda x: freq_dict[x]['count'], reverse=True)[:10]
            for index,key in enumerate(top_10):
                print('{}.) {} appeared {} times'.format(index+1,key, freq_dict[key]['count']))
            break
        elif analysis_type in 'bg':
            while True:
                likely_sentence = []
                try:
                    query = input('What word would you like to search for? ')
                    start = datetime.datetime.now()
                    freq_dict = word_frequency(text_file)
                    bg = bi_gram(text_file,freq_dict,query)
                    x = 0
                    while x in range(10):
                        likely_sentence.append(bg)
                        bg = bi_gram(text_file,freq_dict,bg)
                        x+=1
                    print('The most likely bi-gram pair starting with "{}" is "{} {}". \nThe sentence we created starting with {} is {} {}.'.format(query,query,likely_sentence[0],query, query,' '.join(likely_sentence)))
                    end = datetime.datetime.now()
                    print(end-start)
                    break
                except ValueError:
                    print('Sorry, that word isn\'t used in this text.')
                    break



if __name__ == '__main__':
    # freq_dict = word_frequency('russian_folk_tales.txt')
    # print(freq_dict)
    # print(bi_gram('russian_folk_tales.txt',freq_dict,'Ivan'))
    user_interface()

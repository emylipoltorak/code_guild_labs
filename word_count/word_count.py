import string
from pathlib import Path


def get_text(text_file, remove_common=False):
    # loads a text file and cleans it up for analysis.
    common_words = ['a', 'about', 'all', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come',
                    'could', 'day', 'do', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'he',
                    'her', 'here', 'him', 'his', 'how', 'i', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like',
                    'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one',
                    'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell',
                    'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this',
                    'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when',
                    'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your']

    new_text = 'wordcount_{}'.format(text_file)
    table = str.maketrans({key: None for key in string.punctuation})
    with open(text_file, 'r') as f, open(new_text, 'w') as n_f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('-', ' ').lower().translate(table)
            if remove_common:
                line = line.split()
                line = ' '.join([word for word in line if word not in common_words]) + '\n'
            n_f.write(line)
    return new_text


def word_count(text_file):
    # returns a nested dictionary where the keys are words in text_file and the values are dictionaries
    # containing the count (and eventually the next) values for that word.
    freq_dict = {}
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.split():
                try:
                    if word:
                        freq_dict[word]['count'] += 1
                except KeyError:
                    if word:
                        freq_dict[word] = {}
                        freq_dict[word]['count'] = 1
    return freq_dict


def words_gen(text_file):
    # a generator that will yield the words in text_file one by one.
    for line in text_file:
        for word in line.split():
            yield word


def most_common(lst):
    # returns the most frequently appearing item on a list.
    return max(set(lst), key=lst.count)


def likely_next(text_file, query):
    # returns the word likeliest to follow a given word (query).
    with open(text_file, 'r') as f:
        word_generator = words_gen(f)
        next_words = []
        for word in word_generator:
            if word == query:
                try:
                    next_words.append(next(word_generator))
                except StopIteration:
                    next_words.append('')
    return most_common(next_words)


def interface():
    # command line interface allows the user to select their file and type of analysis.
    while True:
        text_file = Path(input('What file would you like to analyze? '))

        q = input('What would you like to do? Enter 1 for top 10 words, 2 to learn the likeliest next word for a '
                  'given word, or 3 to generate a sentence. ')
        if q is '1':
            exclude = input('Would you like to exclude the 100 most common words? y/n: ').lower()
            if exclude in 'yes':
                new = get_text(text_file, remove_common=True)
            else:
                new = get_text(text_file)
            freq_dict = word_count(new)
            top_10 = sorted(freq_dict, key=lambda x: freq_dict[x]['count'], reverse=True)[:10]
            for index, key in enumerate(top_10):
                print('{}.) {} appeared {} times'.format(index + 1, key, freq_dict[key]['count']))
            break
        elif q is '2':
            new = get_text(text_file)
            query = input('What word would you like to search for? ').lower()
            print('The most likely word to follow {} is {}.'.format(query, likely_next(new, query)))
            break
        elif q is '3':
            new = get_text(text_file)
            query = input('What is the first word in your sentence? ').lower()
            next_word = likely_next(new, query)
            sentence = [query.title(), next_word]
            while True:
                cont = input('Press Y for another word, or N to exit: ').lower()
                print('{}.'.format(' '.join(sentence)))
                if cont in 'n':
                    print('{}.'.format(' '.join(sentence)))
                    break
                elif cont in 'y':
                    next_word = likely_next(new, next_word)
                    sentence.append(next_word)
                else:
                    print('Invalid Input')

        else:
            print('Invalid Input')


if __name__ == '__main__':
    interface()

import string
def get_text(text_file, remove_common=False):
    #loads a text file and cleans it up for analysis.
    common_words = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day',
    'do','even','find','first','for','from','get','give','go','have','he','her','here','him','his','how','i','if',
    'in','into','it','its','just','know','like','look','make','man','many','me','more','my','new','no','not','now',
    'of','on','one','only','or','other','our','out','people','say','see','she','so','some','take','tell','than',
    'that','the','their','them','then','there','these','they','thing','think','this','those','time','to','two',
    'up','use','very','want','way','we','well','what','when','which','who','will','with','would','year','you','your']
    new_text = 'wordcount_{}'.format(text_file)
    table = str.maketrans({key: None for key in string.punctuation})
    with open(text_file, 'r') as f, open(new_text, 'w') as n_f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('-',' ').lower().translate(table)
            if remove_common:
                line = line.split()
                line = ' '.join([word for word in line if word not in common_words])+'\n'
            n_f.write(line)

def word_count(text_file):
    #returns a nested dictionary thats keys are words in text_file, and values are dictionaries
    #containing the count (and eventually the next) values for that word.
    freq_dict = {}
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.split():
                try:
                    if word:
                        freq_dict[word]['count']+=1
                except KeyError:
                    if word:
                        freq_dict[word]={}
                        freq_dict[word]['count']=1
    return freq_dict

def words_gen(text_file):
    #a generator that will yield the words in text_file one by one.
    for line in text_file:
        for word in line.split():
            yield word

def most_common(lst):
    #returns the most frequently appearing item on a list.
    return max(set(lst), key=lst.count)

def likely_next(text_file,query):
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

def bi_gram(text_file,dictionary):
    for key in dictionary:
        dictionary[key]['next']=likely_next(text_file,key)
    return dictionary

def predictive_text(query, dictionary,i):
    #returns a list of the top 10 likeliest words to follow query.
    counter = 0
    sentence = [query]
    for x in range(i):
        sentence.append(dictionary[query]['next'])
        query = dictionary[query]['next']

if __name__ == '__main__':
    metamorphosis = get_text('kafka_metamorphasis.txt')
    kafka_dict = word_count('wordcount_kafka_metamorphasis.txt')
    kafka_bg_dict = bi_gram('wordcount_kafka_metamorphasis.txt',kafka_dict)
    print(predictive_text('samsa',kafka_bg_dict,10))

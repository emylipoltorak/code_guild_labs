def anagram_check(word1,word2):
    word1, word2 = word1.replace(' ',''), word2.replace(' ','')

    if len(word1) == len(word2):
        for letter in word1:
            if letter in word2:
                pass
            else:
                return 'These words are not anagrams.'
            return 'These words are anagrams.'
    else:
        return 'These words are not anagrams.'

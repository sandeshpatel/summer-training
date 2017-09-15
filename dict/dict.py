#!/usr/bin/env python3
import re
import sys
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def build_dict(dictionary_file):
    dictionary = {}
    with open(dictionary_file, 'r') as file:
        for line in file:
            tokens = line.split(' ', 2)
            if len(tokens) < 3:
                continue
            word  = tokens[0].lower()
            meaning = tokens[1] + tokens[2]
            if word not in dictionary:
                dictionary[word] = meaning
            else :
                word = tokens[0].lower()+ ' ' + tokens[1].lower()
                meaning = tokens[2]
                dictionary[word.lower()] = meaning
    return dictionary

def search_word(word, dictionary):
    if word in dictionary:
        print(word)
        print(dictionary[word])
    else:
        nearest = correction(word)
        print('word not found')
        if nearest in dictionary:
            print('did you mean: ' + nearest)
            print(dictionary[nearest])
            print('if you did not ment this')
        print('make sure that spelling is correct')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please enter the word')
        word = input()
    else:
        word = sys.argv[1]

    dictionary = build_dict('dictionary.txt')
    search_word(word.lower(), dictionary)

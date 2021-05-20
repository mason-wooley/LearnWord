from flask import Flask
from nltk.corpus import wordnet
from itertools import islice
import random






"""
# Sample random outputs
running = True
words = 0

while running:
    # Negative number entered breaks the loop
    if words < 0:
        break
    
    if words == 0:
        # Be kind; only enter numbers
        words = int(input('Enter the number of words to fetch:'))
    else:
        # Print X random words where X is input
        word = random.choice(list(words_dict.items()))[0]
        print("{0} — {1}\nEg. {2}".format(word, words_dict[word]['definition'], words_dict[word]['example']))
        words -= 1
"""        
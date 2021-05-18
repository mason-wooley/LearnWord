import requests
from nltk.corpus import wordnet
from itertools import islice
import re
import random

# words.txt sourced from https://github.com/dwyl/english-words
# Filename of words list - 466k English words
filename = "media/words.txt"


# Build dictionary of words
words_dict = {}

print("Building dictionary...")
with open(filename, 'r') as input_file:
    for line in input_file:
        word = line.strip()
        syns = wordnet.synsets(word)
        if syns:
            words_dict[word] = syns[0].definition()

print("{0} words imported.".format(len(words_dict)))

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
        print("{0} — {1}".format(word, words_dict[word]))
        words -= 1
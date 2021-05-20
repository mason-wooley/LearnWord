from flask import Flask

from itertools import islice
from db.build_db import build_db
import random

# Do not run this unless the DB needs to be rebuilt
# build_db()

# Flask stuff
app = Flask(__name__)

@app.route('/')
def hello_word():
    return '<p>Hello, world!</p>'

@app.route('/define/<word>') 
def define(word):
    return 'Looking up the definition of {0}....'.format(word)

if __name__ == "__main__": # on running python app.py
    app.run(debug=True)

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
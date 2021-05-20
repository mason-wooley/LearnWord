from db.connect import connect
from nltk.corpus import wordnet
import psycopg2

# words.txt sourced from https://github.com/dwyl/english-words
# words list includes 466k English words

def build_db(filename='media/words.txt'):
    # Establish connection to PostgreSQL DB
    conn = connect()
    # Cursor object
    cur = conn.cursor()

    print('Building dictionary...')
    with open(filename, 'r') as input_file:
        for line in input_file:
            # Word in words.txt
            word = line.strip()
            # Definition from wordnet
            syns = wordnet.synsets(word)
            # If a definition exists
            if syns:
                sql = """INSERT INTO dictionary(word, definition)
                        VALUES(%s, %s);"""
                # TODO - Add error checking here
                cur.execute(sql, (word, syns[0].definition()))
                conn.commit()
        cur.close()
        conn.close()
    print("Words added to DB")
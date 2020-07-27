import re

filename = "media/Oxford English Dictionary.txt"

read_words = 500

file = open(filename, "r")

type_list = []

for i, line in enumerate(file):
    if read_words == 0 or line is None:
        break

    if len(line.strip()) > 1:
        read_words -= 1
        word_data = line.split("  ")
        word = word_data[0].strip()
        definition = re.sub(r'â€.', '', word_data[1].strip())
        print (word, "—", definition)

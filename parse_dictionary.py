import re

filename = "media/Oxford English Dictionary.txt"

read_words = 500

file = open(filename, "r")

type_list = set()

for i, line in enumerate(file):
    if read_words == 0 or line is None:
        break

    if len(line.strip()) > 1:
        read_words -= 1
        word_data = line.split("  ")
        word = word_data[0].strip()
        definition = re.sub(r'â€.', '', word_data[1].strip())
        def_data = definition.split(" ")
        type_list.add(def_data[0])
        data = []
        cur = ""
        for d in def_data:
            if cur == "":
                cur = d
            else:
                cur += ' ' + d
            if cur.contains("."):
                data.append[cur]
                cur = ""

        print(word, "—", data)

print(type_list)

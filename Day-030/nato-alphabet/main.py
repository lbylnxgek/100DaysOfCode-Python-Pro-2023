import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)


def convert_to_nato_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_phonetic = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet allowed.")
        convert_to_nato_phonetic()
    else:
        print(word_phonetic)


convert_to_nato_phonetic()

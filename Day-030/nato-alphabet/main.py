import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)

word = input("Enter a word: ").upper()
# print(word)

word_phonetic = [nato_dict[letter] for letter in word]
print(word_phonetic)

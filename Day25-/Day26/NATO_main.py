import pandas

data = pandas.read_csv("NATO.csv")

nato = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato)

word = list(input("enter a word: ").upper())
print(word)

new_word = [nato[letter] for letter in word]
print(new_word)

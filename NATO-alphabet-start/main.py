#TODO 1. Create a dictionary in this format:
import pandas as pd

nato_data = pd.read_csv('nato_phonetic_alphabet.csv')
nato = {row['letter']: row['code'] for _, row in nato_data.iterrows()}
print(nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Give me a word to convert to the Nato Alphabet: ").upper()
result = [nato[letter] for letter in word]
print(result)



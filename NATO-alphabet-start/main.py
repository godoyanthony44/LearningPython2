
import pandas as pd

nato_data = pd.read_csv('nato_phonetic_alphabet.csv')
nato = {row['letter']: row['code'] for _, row in nato_data.iterrows()}
print(nato)


def generator():

    word = input("Give me a word to convert to the Nato Alphabet: ").upper()
    try:
        result = [nato[letter] for letter in word]
        print(result)
    except KeyError:
        print("Sorry Only letters in the alphabet please.")
        generator()
    else:
        print(result)


generator()





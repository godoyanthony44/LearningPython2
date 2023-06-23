from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("arial", 40, "italic")
FONT_BOLD = ("arial", 60, "bold")
TEXT_COLOR = 'black'

language = 'Spanish'
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/data.csv")
data = data.to_dict(orient="records")
word = choice(data)
word_spanish, word_english = word['Spanish Word'], word['English Word']


# Choosing a random Spanish word
def new_card():
    global word, word_spanish, word_english, language, flip_timer
    window.after_cancel(flip_timer)
    language = 'Spanish'
    word = choice(data)
    word_spanish, word_english = word['Spanish Word'], word['English Word']
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(card_language_text, text=f'{language}', fill=TEXT_COLOR)
    canvas.itemconfig(card_word_text, text=f'{word_spanish}', fill=TEXT_COLOR)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global language
    language = 'English'
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(card_language_text, text=f'{language}', fill='white')
    canvas.itemconfig(card_word_text, text=f'{word_english}', fill='white')


def is_known():
    data.remove(word)
    data2 = pd.DataFrame(data)
    data2.to_csv("data/words_to_learn.csv", index=False)
    print(len(data))
    new_card()


# Ui Setup
window = Tk()
window.title("Flash Learner")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

card = canvas.create_image(400, 263, image=card_front_image)
card_language_text = canvas.create_text(400, 150, text=f'{language}', font=FONT, fill=TEXT_COLOR)
card_word_text = canvas.create_text(400, 263, text=f'{word_spanish}', font=FONT_BOLD, fill=TEXT_COLOR)

wrong_button = Button(image=wrong_button_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                      command=new_card)
right_button = Button(image=right_button_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                      command=is_known)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

window.mainloop()

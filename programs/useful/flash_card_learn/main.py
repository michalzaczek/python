BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
from random import choice

try:
    words_df = pd.read_csv('data/words_to_learn.csv', index_col='French')
except FileNotFoundError:
    words_df = pd.read_csv('data/french_words.csv', index_col='French')

def next_card():
    global french_word
    try:
        french_word = choice(words_df.index)
        canvas.itemconfig(card_image, image=card_back_img)
        canvas.itemconfig(card_title, text='French')
        canvas.itemconfig(card_word, text=french_word)
        window.after(3000, flip_card)
    except IndexError:
        canvas.itemconfig(card_title, text='You already know all words')
        canvas.itemconfig(card_word, text='Update your words list', font=('Arial', 40, 'bold'))

def flip_card():
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=words_df.loc[french_word, 'English'])

def known():
    words_df.drop(french_word, inplace=True)
    words_df.to_csv('data/words_to_learn.csv')
    next_card()

window = Tk()
window.title('Flashcard Learning Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='Yoy already know all words', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Please update your words_to_learn list', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

button_right = Button(image=right_img, highlightthickness=False, command=known)
button_right.grid(row=1, column=0)

button_wrong = Button(image=wrong_img, highlightthickness=False, command=next_card)
button_wrong.grid(row=1, column=1)

next_card()

window.mainloop()

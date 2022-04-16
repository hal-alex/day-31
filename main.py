import random
from tkinter import *

import pandas
from pandas import *
from random import choice



BACKGROUND_COLOR = "#B1DDC6"

word_data = pandas.read_csv("./data/french_words.csv")
word_dict = word_data.to_dict(orient="records")

print(word_dict)

def approve():
    generate_new_word()

def reject():
    generate_new_word()

def generate_new_word():

    random_word = random.choice(word_dict)
    french_word = random_word["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)







window = Tk()
window.title("French/English Word Guessing Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

approve_image = PhotoImage(file="./images/right.png")
approve_button = Button(text="", image=approve_image, highlightthickness=0, command=approve)
approve_button.grid(column=1, row=1)

reject_image = PhotoImage(file="./images/wrong.png")
reject_button = Button(text="", image=reject_image, highlightthickness=0, command=reject)
reject_button.grid(column=0, row=1)

card_title = canvas.create_text(400, 150, text="French", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 250, text="Word", font=("Arial", 42, "bold"))

generate_new_word()

window.mainloop()
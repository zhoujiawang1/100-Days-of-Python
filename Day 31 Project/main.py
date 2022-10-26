from email.mime import image
from tkinter import PhotoImage
import pandas
from random import choice

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ****************************** Words Handling*********************************

data = pandas.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")


# ***************************** Flash Card ************************************

def switch_word():
    global card_flipper, word_choice
    window.after_cancel(card_flipper)
    word_choice = choice(data)
    canvas.itemconfig(word, text=word_choice["French"])
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(card, image=front_img)
    card_flipper = window.after(3000, func=flip_card)


def flip_card():
    global word_choice
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=word_choice["English"])


# **************************** UI SETUP **************************************
# creating window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_flipper = window.after(3000, func=flip_card)

# loading images
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# canvas
canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 526/2, image=front_img)
language = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# creating buttons
wrong_button = Button(image=wrong_button_img,
                      highlightthickness=0, bg=BACKGROUND_COLOR, command=switch_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_img,
                      highlightthickness=0, bg=BACKGROUND_COLOR, command=switch_word)
right_button.grid(row=1, column=1)


window.mainloop()

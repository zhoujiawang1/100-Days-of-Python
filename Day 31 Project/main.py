from email.mime import image
from tkinter import PhotoImage


from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# **************************** UI SETUP **************************************

# creating window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# loading images
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# canvas
canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 526/2, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

# creating buttons
wrong_button = Button(image=wrong_button_img,
                      highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_img,
                      highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)


window.mainloop()

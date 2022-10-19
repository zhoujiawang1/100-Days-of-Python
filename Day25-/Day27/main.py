from tkinter import *
import turtle


def button_click():
    # my_label["text"] = "button has been clicked"
    print(entry.get())
    my_label["text"] = entry.get()


# creates GUI
window = Tk()
window.title("GUI")

# minimum size
window.minsize(width=500, height=300)

# create label
my_label = Label(text="Label", font=("Arial", 24, "bold"))

my_label["text"] = "Next text"
my_label.config(text="New text again")

######
# layout section
# my_label.pack()
# place: layout manager, can provide x and y value
# top left is (0,0)
# my_label.place(x=200, y=100)
my_label.grid(column=0, row=0)


# creates button
button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

# creates entry
entry = Entry(width=10)
# entry.pack()
entry.grid(column=2, row=2)


window.mainloop()

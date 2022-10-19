from tkinter import *


def convert():
    km["text"] = str(int(miles.get()) * 1.6)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

label = Label(text="is equal to ")
label.grid(row=1, column=2)

m_label = Label(text=" Miles")
m_label.grid(row=0, column=4)

k_label = Label(text=" km")
k_label.grid(row=1, column=4)

miles = Entry(width=10)
miles.grid(row=0, column=3)

km = Label(text="0")
km.grid(row=1, column=3)

convert = Button(text="Convert", command=convert)
convert.grid(row=2, column=3)

window.mainloop()

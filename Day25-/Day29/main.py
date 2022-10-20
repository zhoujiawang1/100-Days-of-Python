from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

w_label = Label(text="Website:")
w_label.grid(row=1, column=0)
u_label = Label(text="Email/Username:")
u_label.grid(row=2, column=0)
p_label = Label(text="Password:")
p_label.grid(row=3, column=0)


website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2)
password = Entry(width=21)
password.grid(row=3, column=1)


p_gen = Button(text="Generate Password")
p_gen.grid(row=3, column=2)
add_b = Button(text="Add", width=36)
add_b.grid(row=4, column=1)


window.mainloop()

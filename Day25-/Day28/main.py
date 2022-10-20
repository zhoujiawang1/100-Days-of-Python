import time
from tabnanny import check
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_work():
    time_work = 0.05*60
    countdown(time_work)
    title.config(text="Work!", fg=GREEN)


def start_break():
    time_break = 0.1*60
    countdown(time_break)
    title.config(text="Break", fg=RED)


def start_long_break():
    time_break = 0.15*60
    countdown(time_break)
    title.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(timer):
    global reps
    new_timer = time.strftime("%M:%S", time.gmtime(timer))
    canvas.itemconfig(timer_text, text=new_timer)

    if timer == 0:
        reps += 1

    if timer > 0:
        window.after(1000, countdown, timer-1)
    elif reps % 8 == 0:
        start_long_break()
    elif reps % 2 == 0 and reps != 0:
        start_break()

    else:
        start_work()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", font=(
    FONT_NAME, 35, "bold"), fill="white")

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 24, "bold"), bg=YELLOW)

start = Button(text="Start", command=start_work)
reset = Button(text="Reset")

title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start.grid(row=2, column=0)
checkmark.grid(row=3, column=1)
reset.grid(row=2, column=2)


window.mainloop()

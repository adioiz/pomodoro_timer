from tkinter import *
import math
from setuptools import Command
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
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    reps = 0
    check_mark.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    time = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=time) #change the timer text every iteration
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor((reps-1)/2)):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

# Create canvas and photo image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # The size of the photo
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # x & y sizes locate the tomato image in the center of the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Create labels and buttons
title_label = Label(text="Timer", font=(FONT_NAME, 50))
title_label.grid(column=2, row=1)
title_label.config(bg=YELLOW, fg=GREEN)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer) 
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

check_mark = Label(text="", bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=4)



window.mainloop()
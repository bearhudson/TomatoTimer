#!/usr/bin/python3

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
start_button = None


# ---------------------------- TIMER RESET ------------------------------- #
def restart_timer():
    global start_button
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title.config(text='Timer')
    reps = 0
    start_button.config(text='Start', command=start_timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global start_button

    def stop_timer():
        window.after_cancel(timer)

    global reps
    reps += 1
    start_button.config(text='Stop', command=stop_timer)
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text='Break!', fg=PINK)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        title.config(text='Break!', fg=RED)
        count_down(short_break_seconds)
    else:
        title.config(text='Work:(', fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global reps
    global timer
    count_min = math.floor(seconds / 60)
    count_seconds = seconds % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if seconds > 0:
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        check_mark = ""
        for _ in range(math.floor(reps / 2)):
            check_mark += '✔'
        check_marks.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title.grid(row=0, column=1)
canvas.create_image(100, 110, image=tomato_image)
timer_text = canvas.create_text(100, 143, text="00:00", fill=YELLOW, font=(FONT_NAME, 40, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(row=3, column=0)

restart_button = Button(text='Restart', command=restart_timer, highlightthickness=0)
restart_button.grid(row=3, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()

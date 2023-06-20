from tkinter import *
import math

TIMER_FONT = ("Courier", 60, "bold")
FONT = ("Courier", 40, "bold")
WORK_MIN = 25
current_time = '00:00'
SHORT_MIN_BREAK = 5
LONG_MIN_BREAK = 20
LAVENDER = '#e6e3a1'
FRENCH_GREY = '#FFFFFF'
FRENCH_GREY2 = '#000000'
reps = 1

window = Tk()
window.config(padx=100,pady=50,width=500, height=300, bg=LAVENDER)
window.title("Pomo App")


def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_sec_break = SHORT_MIN_BREAK*60
    long_sec_break = LONG_MIN_BREAK*60
    check_marks = ''.join(['✔' for i in range(reps)])
    check_text.config(text=f'{check_marks}')
    start_button.config(command='')

    if reps % 2 != 0:
        countdown(work_sec)
        label.config(text="Work!",fg='#53ed68')
        reps += 1
    elif reps % 2 == 0 and reps != 8:
        countdown(short_sec_break)
        label.config(text="Short Break", fg='#40f5f2')
        reps += 1
    else:
        countdown(long_sec_break)
        label.config(text="Long Break", fg='#535ded')
        reps = 0


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec <= 9:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global counter
        counter = window.after(1000, countdown, count-1)


def reset():
    global reps
    canvas.itemconfig(timer_text, text=f"{current_time}")
    label.config(text="Pomodoro Timer", fg=FRENCH_GREY2)
    check_text.config(text='')
    start_button.config(command=start_timer)
    window.after_cancel(counter)
    reps = 1


canvas = Canvas(width=400,height=400, bg=LAVENDER, highlightthickness=0)
photo = PhotoImage(file='potato.png')
label = Label(text="Pomodoro Timer", font=FONT, fg=FRENCH_GREY2, bg=LAVENDER)
start_button = Button(text="Start", font=FONT, command=start_timer)
reset_button = Button(text="Reset", font=FONT, command=reset)

check_text = Label(text='', font=FONT, bg=LAVENDER, fg='green')

canvas.create_image(200, 200, image=photo)
timer_text = canvas.create_text(200, 210, text=f"{current_time}", font=TIMER_FONT, fill='white')

canvas.grid(column=1, row=1, pady=(0, 50))
label.grid(column=1, row=0, pady=(0, 50))
start_button.grid(column=0, row=2)
reset_button.grid(column=2,row=2)
check_text.grid(column=1,row=3)

window.mainloop()


import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None

reps = 0
# explanation about reps: rep 1 is 25 min work, rep 2 is 5 min break,
# so on, so reps 1/3/5/7 are 25 min works, reps 2/4/6 are 5 min breaks
# and rep 8 is 20 min break

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    timer_sign.config(text="Timer")
    global reps
    reps = 0
    checkmark.config(text="")
    start_button.config(state="active")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global reps
    global timer_sign
    global start_button
    start_button.config(state="disabled")
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_sign.config(text="Study", fg=GREEN)
    elif reps % 2 == 0 and reps % 8 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_sign.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_sign.config(text="Break", fg=RED)

    # count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global checkmark
    count_min = count // 60
    count_sec = "{:02d}".format(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        raise_window()
        timer_start()
        mark = ""
        work_sessions = math.floor(reps % 8 / 2)
        for i in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)
        # if reps % 2 == 0:
        #     checkmark_num = (reps % 8) / 2
        #     display ="✔"
        #     for i in range(checkmark_num):
        #         display = f"{display}✔"
        #     checkmark.config(text=f"{display}")

# ------------------------- BRING POMODORO TO FRONT----------------------
def raise_window():
    window.attributes("-topmost", True)
    window.attributes("-topmost", False)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# TIMER SIGN
timer_sign = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_sign.grid(column=2, row=1)

# COUNT_DOWN FUNCTION BEGINS
# count_down(10)

# START BUTTON
start_button = tkinter.Button(text="Start", command=timer_start)
start_button.grid(column=1, row=3)

# RESET BUTTON
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

# CHECKMARK(FOR HOW MANY CYCLES OF POMODORO YOU'VE DONE) SIGN
checkmark = tkinter.Label(text="", bg=YELLOW, fg=GREEN)
checkmark.grid(column=2, row=4)

window.mainloop()




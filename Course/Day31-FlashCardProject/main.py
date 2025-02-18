from tkinter import *
from tkinter import messagebox
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    print(len(to_learn))
    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_image, image=card_front_image)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)
    else:
        messagebox.showinfo(title="Congratulations!", message="You have completed learning French.")


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def known_card():
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        to_learn_dataframe = pandas.DataFrame(to_learn)
        to_learn_dataframe.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    else:
        messagebox.showinfo(title="Congratulations!", message="You have completed learning French.")


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_image, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

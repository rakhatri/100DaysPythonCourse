from tkinter import *


def button_click():
    my_label_3.config(text=round(float(input_text.get()) * 1.60934, 2))


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input_text = Entry(width=10)
input_text.grid(column=1, row=0)


my_label_1 = Label(text="Miles")
my_label_1.grid(column=2, row=0)
my_label_1.config(padx=10, pady=10)

my_label_2 = Label(text="is equal to")
my_label_2.grid(column=0, row=1)

my_label_3 = Label(text="0")
my_label_3.grid(column=1, row=1)

my_label_4 = Label(text="Km")
my_label_4.grid(column=2, row=1)

button_1 = Button(text="Calculate", command=button_click)
button_1.grid(column=1, row=3)


window.mainloop()

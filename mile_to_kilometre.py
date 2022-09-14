from tkinter import *


window = Tk()
window.title("Miles to Kilometres Calculator")
window.config(padx=20, pady=20)


def calculate():
    if entry.get() == '':
        km_blank = 0
        answer_label["text"] = str(km_blank)
    else:
        miles = float(entry.get())
        km = miles * 1.60934
        answer_label["text"] = str(km)
        

entry = Entry(width=7)
entry.grid(row = 0, column = 1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row = 1, column = 0)

answer_label = Label(text="")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row = 2, column = 1)





window.mainloop()
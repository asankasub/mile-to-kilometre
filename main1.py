def button_clicked():
    label = print("I got clicked")
    my_label["text"] = input.get()


from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)


# #Label

my_label = Label(text = "I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)


#Button

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button1 = Button(text="Click Me")
button1.grid(row=0, column=2)



# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum



# # print(add(2, 3, 4, 5, 6))

# def calculate(**kwargs):



#Entry

input = Entry(width=10)
print(input.get())
input.grid(row=3, column=3)












window.mainloop()
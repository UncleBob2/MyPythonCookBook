from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color Chooser")
root.geometry("400x1200")


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label1 = Label(root, text='You Picked a color!',
                      font=('Helvetica', 32), bg=my_color).pack()


my_buttom = Button(root, text='Pick a color', command=color).pack()


root.mainloop()

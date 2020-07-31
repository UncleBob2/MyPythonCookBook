# My Computer Science Glossary Project

import tkinter as tk
from PIL import ImageTk, Image

# exit key function


# define click
def click():
    entered_text = textentry.get()  # this collects from the entry box
    output.delete(0.0, tk.END)
    try:
        define = my_dic[entered_text]
    except:
        define = "Sorry try again"
    output.insert(tk.END, define)


def close_window():
    window.destroy()
    exit()


##### main######
window = tk.Tk()  # calling tkinter func/class to create an object called window
window.title("My Computer Science Glossary")
window.config(background="black")

# My photo
picture = tk.Canvas(window, width=350, height=400)
picture.grid(row=0, column=0, sticky=tk.S)

photo1 = ImageTk.PhotoImage(
    Image.open("/Users/winsorhoang/dev/python/projects/tkinter basics/sketch.png")
)


picture.create_image(70, 50, image=photo1, anchor=tk.NW)
# create label 1
l1 = tk.Label(
    window,
    text="I am Alexa, how can I help you?",
    bg="black",
    fg="white",
    font="None 15 bold",
)
l1.grid(row=1, column=0)

# create label 2
l2 = tk.Label(
    window, text="Enter a word: ", bg="black", fg="yellow", font="None 15 bold"
)
l2.grid(row=2, column=0, sticky=tk.W)

# create a text entry box
textentry = tk.Entry(window, width=30, bg="white")
textentry.grid(row=2, column=0, sticky=tk.E)

# create a submit button
submit = tk.Button(
    window,
    text="SUBMIT",
    bg="gray",
    width=6,
    command=click,
    font="Arial 12",
    relief=tk.RAISED,
)
submit.grid(row=3, column=0, stick=tk.E)

# create definition label

l3 = tk.Label(window, text="Definition: ", bg="black", fg="yellow", font="None 15 bold")
l3.grid(row=4, column=0, sticky=tk.W)


# create a text box
output = tk.Text(window, width=75, height=20, wrap=tk.WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=tk.W)

my_dic = {
    "algo": "step by step instructions to complete a task",
    "bug": "undocumented options that crashes a program",
}

# add a exit button
Bexit = tk.Button(window, text="Exit", width=14, command=close_window)
Bexit.grid(row=6, column=0, sticky=tk.E)


# run the main loop
window.mainloop()


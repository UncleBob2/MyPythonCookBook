from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Alogrithm Visualizer")
root.geometry('1000x600+200+80')
root.config(bg='#c0c0c0')


def drawData(data):
    canvas_width = 970
    canvas_height = 450
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_bar = 10

    for i, heigh


def Generate():
    print('Selected Alogrithm: ' + selected_algorithm.get())


selected_algorithm = StringVar()
# lable, buttons, speed scale

mainlabel = Label(root, text='Alogrithm : ', font=(
    'arial', 24, 'italic bold'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
mainlabel.place(x=0, y=0)

mainlabel = Label(root, text="Alogrithm")

algo_menu = ttk.Combobox(root, width=12, font=('arial', 24, 'italic'), textvariable=selected_algorithm, values=[
                         'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Radix Sort'])
algo_menu.place(x=240, y=0)
algo_menu.current(0)  # default Bubble Sort


samplesizelabel = Label(root, text='Sample Size : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
samplesizelabel.place(x=0, y=60)
samplesize = Scale(root, from_=0, to=30, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
samplesize.place(x=150, y=60)

minvaluelabel = Label(root, text='Min Value: ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
minvaluelabel.place(x=275, y=60)
minvalue = Scale(root, from_=0, to=10, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
minvalue.place(x=425, y=60)

maxvaluelabel = Label(root, text='Max Value : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
maxvaluelabel.place(x=550, y=60)
maxvalue = Scale(root, from_=0, to=100, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
maxvalue.place(x=700, y=60)


start = Button(root, text='Start', bg='#005392', fg='blue', font=('arial', 24, 'italic'), relief=SUNKEN,
               activebackground='white', activeforeground='white', bd=5, width=10)
start.place(x=830, y=0)

random_generate = Button(root, text='Generate', bg='#7980ff', fg='blue',  font=('arial', 24, 'italic'),
                         relief=SUNKEN, activebackground='white', activeforeground='white', bd=5, width=10, command=Generate)
random_generate.place(x=830, y=60)


speedlabel = Button(root, text='Speed : ', bg='#005392', fg='black', font=('arial', 24, 'italic'), relief=SUNKEN,
                    bd=5, width=10)
speedlabel.place(x=550, y=0)

speedscale = Scale(root, from_=0.1, to=5, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)

speedscale.place(x=700, y=0)

canvas = Canvas(root, width=970, height=450, bg='black')
canvas.place(x=10, y=120)

root.mainloop()

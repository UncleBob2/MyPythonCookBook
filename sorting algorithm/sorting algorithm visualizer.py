from tkinter import *
import time
from tkinter import ttk
import random


root = Tk()
root.title("Sorting Alogrithm Visualizer")
root.geometry('1100x600+200+80')
root.config(bg='#c0c0c0')
#data = []


def drawData(data, colorArray):
    canvas.delete('all')
    canvas_width = 1070
    canvas_height = 450
    x_width = canvas_width / (len(data))
    offset = x_width / 10
    spacing_bet_bars = x_width / 10
    normalized_data = [i / max(data) for i in data]
    root.update_idletasks()
    root.update_idletasks()  # Needed on MacOS -- see #34275.
    root.lift()  # work around bug in Tk 8.5.18+ (issue #24570)

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_bars
        y0 = canvas_height - height * 400  # normalized so that we don't exceed our canvas
        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(
            x0 + 2, y0, anchor=SW, text=str(data[i]), font=('arial', 15, 'italic'), fill='orange')


def Buble_Sort(data, drawData, timeTick):
    for k in range(len(data) - 1):
        # based on sudo code above where by k start from 1 and i from 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                drawData(data, ['yellow' if x == i or x == i +
                                1 else '#A90042' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['yellow' for x in range(len(data))])


def StartAlgorithm():
    global data
    Buble_Sort(data, drawData, speedscale.get())


def Generate():
    global data
    print('Selected Alogrithm: ' + selected_algorithm.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sampleisize = int(samplesize.get())

    data = []
    for i in range(sampleisize):
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawData(data, ['#A90042' for x in range(len(data))])


selected_algorithm = StringVar()
# lable, buttons, speed scale

mainlabel = Label(root, text='Alogrithm : ', font=(
    'arial', 24, 'italic bold'), bg="#eaeaea",  width=10, fg='black', relief=GROOVE, bd=2)
mainlabel.place(x=10, y=10)

mainlabel = Label(root, text="Alogrithm")

algo_menu = ttk.Combobox(root, width=11, font=('arial', 20, 'italic'), textvariable=selected_algorithm, values=[
                         'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Radix Sort'])
algo_menu.place(x=160, y=10)
algo_menu.current(0)  # default Bubble Sort


samplesizelabel = Label(root, text='Sample Size : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=13, fg='black', relief=GROOVE, bd=2)
samplesizelabel.place(x=10, y=60)
samplesize = Scale(root, from_=10, to=100, bg='#7980ff', resolution=10, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
samplesize.set(10)
samplesize.place(x=150, y=60)


minvaluelabel = Label(root, text='Min Value: ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
minvaluelabel.place(x=275, y=60)
minvalue = Scale(root, from_=1, to=10, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
minvalue.set(1)
minvalue.place(x=425, y=60)


maxvaluelabel = Label(root, text='Max Value : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
maxvaluelabel.place(x=550, y=60)
maxvalue = Scale(root, from_=10, to=100, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
maxvalue.set(100)
maxvalue.place(x=700, y=60)


start = Button(root, text='Start Sort', bg='#005392', fg='blue', font=('arial', 24, 'italic'), relief=SUNKEN,
               activebackground='white', activeforeground='white', bd=5, width=15, command=StartAlgorithm)
start.place(x=830, y=10)


random_generate = Button(root, text='Generate Data', bg='#7980ff', fg='blue',  font=('arial', 24, 'italic'),
                         relief=SUNKEN, activebackground='white', activeforeground='white', bd=5, width=15, command=Generate)
random_generate.place(x=830, y=60)


speedlabel = Button(root, text='Speed : ', bg='#005392', fg='black', font=('arial', 24, 'italic'), relief=SUNKEN,
                    bd=5, width=6)
speedlabel.place(x=550, y=10)
speedscale = Scale(root, from_=0.1, to=5, bg='#7980ff', resolution=0.2, length=160, digits=2, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
speedscale.place(x=640, y=10)


canvas = Canvas(root, width=1070, height=450, bg='black')
canvas.place(x=10, y=120)

root.mainloop()

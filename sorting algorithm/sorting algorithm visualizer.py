from tkinter import *
import time
from tkinter import ttk
import random
import sys


root = Tk()
root.title("Sorting Alogrithm Visualizer")
root.geometry('1100x600+200+80')
root.config(bg='#c0c0c0')
data = []


def drawData(data, colorArray):
    canvas.delete('all')
    canvas_width = 1070
    canvas_height = 450
    x_width = canvas_width / (len(data))
    offset = x_width / 10
    spacing_bet_bars = x_width / 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_bars
        y0 = canvas_height - height * 400  # normalized so that we don't exceed our canvas
        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(
            x0 + 2, y0, anchor=SW, text=str(data[i]), font=('arial', 15, 'italic'), fill='orange')
    root.update()


def Bubble_Sort(data, drawData, timeTick):
    print('Begin Bubble Sort')
    for k in range(len(data) - 1):
        # based on sudo code above where by k start from 1 and i from 0
        for i in range(len(data) - 1):
            drawData(data, ['yellow' if x == i or x == i +
                            1 else '#A90042' for x in range(len(data))])
            time.sleep(timeTick)
            print('compare ', data[i], data[i + 1])
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

    drawData(data, ['yellow' for x in range(len(data))])


def Selection_Sort(data, drawData, timeTick):
    print('Begin Selection Sort')
    for i in range(len(data) - 1):
        iMin_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[iMin_index]:
                iMin_index = j
        if iMin_index != i:
            data[i], data[iMin_index] = data[iMin_index], data[i]
            drawData(data, ['yellow' if x == i or x == iMin_index
                            else '#A90042' for x in range(len(data))])
            time.sleep(timeTick)

    drawData(data, ['yellow' for x in range(len(data))])


def Insertion_Sort(data, drawData, timeTick):
    print('Begin Insertion Sort')
    for i in range(1, len(data)):
        value = data[i]
        hole = i
        while(hole > 0 and data[hole - 1] > value):
            data[hole] = data[hole - 1]
            hole = hole - 1
            drawData(data, ['yellow' if x == hole or x == i
                            else '#A90042' for x in range(len(data))])
            time.sleep(timeTick)
        data[hole] = value
    drawData(data, ['yellow' for x in range(len(data))])


def Merge_Sort(data, drawData, timeTick):
    print('Begin Merge Sort')
    n = len(data)
    if (n < 2):
        return  # based condition
    mid = n // 2
    left_half = data[0:mid]  # up to but not including mid
    right_half = data[mid:]  # from mid to end of array
    for i in range(0, mid - 1):  # i = 0 to mid -1
        left_half[i] = data[i]
        drawData(data, ['yellow' if x == i
                        else '#A90042' for x in range(mid - 1)])
    for i in range(mid, n - 1):  # i = mid to n-1
        right_half[i - mid] = data[i]
        drawData(data, ['yellow' if x == i
                        else '#A90042' for x in range(n - 1)])
    Merge_Sort(left_half)
    Merge_Sort(right_half)
    merge(left_half, right_half, data)
    drawData(data, ['yellow' for x in range(len(data))])
    time.sleep(timeTick)


def merge(left_half, right_half, data, drawData, timeTick):
    nL = len(left_half)
    nR = len(right_half)
    i, j, k = 0, 0, 0
    while (i < nL and j < nR):
        if (left_half[i] <= right_half[j]):
            data[k] = left_half[i]
            i += 1
        else:
            data[k] = right_half[j]
            j += 1
        k += 1
    while(i < nL):
        data[k] = left_half[i]
        i += 1
        k += 1
    while(j < nR):
        data[k] = right_half[j]
        j += 1
        k += 1


def Quick_Sort(data, low, high, drawData, timeTick):
    print(data, low, high)
    if (low < high):
        border = partition(data, low, high, drawData, timeTick)
        print('left partition sort from index', data[low:border])
        Quick_Sort(data, low, border - 1, drawData, timeTick)
        print('right partition sort from index', data[border + 1: high])
        Quick_Sort(data, border + 1, high, drawData, timeTick)

    if len(data) - 1 == high:
        print('FINAL CUT')
        drawData(data, ['yellow' for x in range(len(data))])


def partition(data, low, high, drawData, timeTick):

    pivotValue = data[high]  # last element as pivot
    # <smaller values> <pivot> <larger values>
    print('pivotValue: ', pivotValue)
    border = low
    print('border', data[low])

    drawData(data, QuickSortColor(len(data), low, high, border, border))
    time.sleep(timeTick)
    for i in range(low, high):
        print(i)
        if (data[i] <= pivotValue):
            drawData(data, QuickSortColor(
                len(data), low, high, border, i, True))
            time.sleep(timeTick)
            if (data[i] != data[border]):
                print('swapping', data[i], data[border])
            data[i], data[border] = data[border], data[i]
            border += 1
        drawData(data, QuickSortColor(len(data), low, high, border, i))
        time.sleep(timeTick)

    print('swapping pivot and border, pivot is now in correct position ', data[high],
          data[border])
    drawData(data, QuickSortColor(len(data), low, high, border, low, True))
    time.sleep(timeTick)

    data[border], data[high] = data[high], data[border]
    return border


def QuickSortColor(datalen, low, high, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(datalen):
        # color when no operation is performed or base coloring
        if i >= low and i <= high:
            colorArray.append('green')
        else:
            colorArray.append('yellow')
        if i == high:
            colorArray[i] == 'orange'
        elif i == border:
            colorArray[i] == 'white'
        elif i == currIdx:
            colorArray[i] = 'blue'
    if isSwapping:
        if i == border or i == currIdx:
            colorArray[i] = 'white'
    return colorArray


def StartAlgorithm():
    global data
    print(data)

    if data == []:
        sys.exit()

    if(algo_menu.get() == 'Bubble Sort'):
        Bubble_Sort(data, drawData, speedscale.get())

    elif(algo_menu.get() == 'Selection Sort'):
        Selection_Sort(data, drawData, speedscale.get())

    elif(algo_menu.get() == 'Insertion Sort'):
        Insertion_Sort(data, drawData, speedscale.get())

    elif(algo_menu.get() == 'Merge Sort'):
        Merge_Sort(data, drawData, speedscale.get())

    elif(algo_menu.get() == 'Quick Sort'):
        Quick_Sort(data, 0, len(data) - 1, drawData, speedscale.get())


def Generate():
    global data
    print('Selected Alogrithm: ' + selected_algorithm.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sampleisize = int(samplesize.get())

    data = []
    #data = [2,5,8,1,6,4,3,7]
    for i in range(sampleisize):
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawData(data, ['#A90042' for x in range(len(data))])


selected_algorithm = StringVar()

# GUI, Algo
mainlabel = Label(root, text='Alogrithm : ', font=(
    'arial', 24, 'italic bold'), bg="#eaeaea",  width=10, fg='black', relief=GROOVE, bd=2)
mainlabel.place(x=10, y=10)
mainlabel = Label(root, text="Alogrithm")

# drop down select button
algo_menu = ttk.Combobox(root, width=11, font=('arial', 20, 'italic'), textvariable=selected_algorithm, values=[
                         'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort'])
algo_menu.place(x=160, y=10)
algo_menu.current(3)  # default Bubble Sort

# sample size selector
samplesizelabel = Label(root, text='Sample Size : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=13, fg='black', relief=GROOVE, bd=2)
samplesizelabel.place(x=10, y=60)
samplesize = Scale(root, from_=10, to=100, bg='#7980ff', resolution=10, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
samplesize.set(10)
samplesize.place(x=150, y=60)

# min value selector
minvaluelabel = Label(root, text='Min Value: ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
minvaluelabel.place(x=275, y=60)
minvalue = Scale(root, from_=1, to=10, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
minvalue.set(1)
minvalue.place(x=425, y=60)

# max value selector
maxvaluelabel = Label(root, text='Max Value : ', font=(
    'arial', 17, 'italic'), bg="#eaeaea",  width=16, fg='black', relief=GROOVE, bd=2)
maxvaluelabel.place(x=550, y=60)
maxvalue = Scale(root, from_=10, to=100, bg='#7980ff', resolution=1, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
maxvalue.set(100)
maxvalue.place(x=700, y=60)

# Start sorting button
start = Button(root, text='Start Sort', bg='#005392', fg='blue', font=('arial', 24, 'italic'), relief=SUNKEN,
               activebackground='white', activeforeground='white', bd=5, width=15, command=StartAlgorithm)
start.place(x=830, y=10)


# random generate data button
random_generate = Button(root, text='Generate Data', bg='#7980ff', fg='blue',  font=('arial', 24, 'italic'),
                         relief=SUNKEN, activebackground='white', activeforeground='white', bd=5, width=15, command=Generate)
random_generate.place(x=830, y=60)


# Delay selector
speedlabel = Button(root, text='Delay : ', bg='#005392', fg='black', font=('arial', 24, 'italic'), relief=SUNKEN,
                    bd=5, width=6)
speedlabel.place(x=550, y=10)
speedscale = Scale(root, from_=0.001, to=0.5, bg='#7980ff', resolution=0.05, length=160, digits=3, orient=HORIZONTAL, font=(
    'arial', 14, 'italic'), relief=GROOVE, bd=2, width=10)
speedscale.set(0.5)
speedscale.place(x=640, y=10)

# define the plotting area
canvas = Canvas(root, width=1070, height=450, bg='black')
canvas.place(x=10, y=120)

root.mainloop()

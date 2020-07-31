import time


def Buble_Sort(data, drawData, timeTick):
    for k in range(1, len(data) - 1):
        # based on sudo code above where by k start from 1 and i from 0
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                drawData(data, ['yellow' if x == i or x == i +
                                1 else '#A90042' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['yellow' for x in range(len(data))])

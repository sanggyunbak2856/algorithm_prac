import random

def selectionSort(data):
    for standard in range(len(data) - 1):
        min = standard
        for index in range(standard + 1, len(data)):
            if data[min] > data[index]:
                min = index
        data[min], data[standard] = data[standard], data[min]
    return data

dataList = random.sample(range(100), 50)
print(selectionSort(dataList))
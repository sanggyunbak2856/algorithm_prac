import sys

inputNum = int(sys.stdin.readline())
inputList = list()

for i in range(inputNum):
    element = sys.stdin.readline().split('\n')[0].split(" ")
    inputList.append((int(element[0]), int(element[1])))

# sort (selection sort)
for index in range(len(inputList) - 1):
    min = index
    for index2 in range(index + 1, len(inputList)):
        if inputList[index2][0] < inputList[min][0]:
            min = index2
        elif inputList[index2][0] == inputList[min][0] and inputList[index2][1] < inputList[min][1]:
            min = index2
    inputList[index], inputList[min] = inputList[min], inputList[index]

# print
for index in range(len(inputList)):
    print(inputList[index][0], inputList[index][1])

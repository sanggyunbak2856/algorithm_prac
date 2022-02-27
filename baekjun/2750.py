import sys

numberOfInput = int(sys.stdin.readline())
data = list()

for i in range(numberOfInput):
    data.append(int(sys.stdin.readline()))

for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

for i in range(len(data)):
    print(data[i])

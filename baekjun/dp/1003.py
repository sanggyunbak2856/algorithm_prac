import sys

dpZero = [0] * 41
dpZero[0] = 1
dpOne = [0] * 41
dpOne[1] = 1

for index in range(2, 41):
    dpZero[index] = dpZero[index - 1] + dpZero[index - 2]
    dpOne[index] = dpOne[index - 1] + dpOne[index - 2]

inputNum = int(sys.stdin.readline())

for i in range(inputNum):
    num = int(sys.stdin.readline())
    print(dpZero[num], dpOne[num])



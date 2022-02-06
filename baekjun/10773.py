import sys

number = int(sys.stdin.readline())
total = 0
stack = list()

for i in range(number):
    inputNum = int(sys.stdin.readline())
    
    if inputNum == 0:
        total -= stack[-1]
        del stack[-1]
    else:
        stack.append(inputNum)
        total += inputNum

print(total)
        
import sys

n = int(sys.stdin.readline())
dp = [0] * n

firstCost = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
minIndex = 0

for i in range(len(firstCost)):
    if firstCost[i] < firstCost[minIndex]:
        minIndex = i
dp[0] = firstCost[minIndex]

for i in range(1, n):
    cost = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
    if minIndex == 0:
        if cost[1] < cost[2]:
            minIndex = 1
        else:
            minIndex = 2
    elif minIndex == 1:
        if cost[0] < cost[2]:
            minIndex = 0
        else:
            minIndex = 2
    elif minIndex == 2:
        if cost[0] < cost[1]:
            minIndex = 0
        else:
            minIndex = 1
    dp[i] = dp[i - 1] + cost[minIndex]
    

print(dp[-1])
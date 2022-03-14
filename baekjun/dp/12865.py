import sys

firstinput = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
number, maxweight = firstinput[0], firstinput[1]

dp = [[0 for __ in range(maxweight + 1)] for __ in range(number + 1)]
w = [0] * number
v = [0] * number

for i in range(number):
    element = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
    w[i], v[i] = element[0], element[1]

for i in range(1, number + 1):
     for j in range(1, maxweight + 1):
         if w[i - 1] > j:
             dp[i][j] = dp[i - 1][j]
         else:
             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

print(dp[number][maxweight])

    

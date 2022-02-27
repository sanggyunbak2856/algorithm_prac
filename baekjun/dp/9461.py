import sys

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for index in range(4, 101):
    dp[index] = dp[index - 3] + dp[index - 2]

inputNum = int(sys.stdin.readline())

for i in range(inputNum):
    num = int(sys.stdin.readline())
    print(dp[num])
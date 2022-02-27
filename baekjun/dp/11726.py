import sys

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2]

num = int(sys.stdin.readline())
print(dp[num]%10007)
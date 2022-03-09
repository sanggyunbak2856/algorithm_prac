import sys

n = int(sys.stdin.readline())

array = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    array[i] = int(sys.stdin.readline())
    if i == 1:
        dp[1] = array[1]
    elif i == 2:
        dp[2] = array[1] + array[2]
    else:
        dp[i] = max(dp[i - 3] + array[i - 1] + array[i], dp[i - 2] + array[i], dp[i - 1])

print(dp[-1])
import sys

n = int(sys.stdin.readline())
dp = [[0, 0, 0] for i in range(n)]
numbers = [list(map(int, sys.stdin.readline().split('\n')[0].split(" "))) for i in range(n)]
dp[0][0], dp[0][1], dp[0][2] = numbers[0][0], numbers[0][1], numbers[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + numbers[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + numbers[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + numbers[i][2]

print(min(dp[n - 1]))
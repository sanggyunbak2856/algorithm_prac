import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
dp = [1] * n

for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
        
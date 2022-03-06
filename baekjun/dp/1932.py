import sys

n = int(sys.stdin.readline())
numbers = list()
dp = [[0 for i in range(j + 1)] for j in range(n)]

for i in range(n):
    number = list(map(int, sys.stdin.readline().split('\n')[0].split(" ")))
    numbers.append(number)

if n == 1:
    print(numbers[0][0])
else:
    dp[0][0] = numbers[0][0]
    dp[1][0] = dp[0][0] + numbers[1][0]
    dp[1][1] = dp[0][0] + numbers[1][1]

    for i in range(2, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + numbers[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + numbers[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + numbers[i][j]
                
    print(max(dp[n-1]))

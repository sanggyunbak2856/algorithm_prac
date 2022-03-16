import sys

array = list(sys.stdin.readline().split('\n')[0])
string = list(sys.stdin.readline().split('\n')[0])
dp = [[0 for __ in range(len(array) + 1)] for __ in range(len(string) + 1)]

st = 0
for i in range(1, len(string) + 1):
    check = False
    for j in range(1, len(array) + 1):
        if array[i-1] == string[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))


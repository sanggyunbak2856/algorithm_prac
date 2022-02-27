import sys
dp = [[[1 for i in range(21)] for j in range(21)] for k in range(21)]

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j and j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

print(dp[10][4][6])
while True:
    nums = sys.stdin.readline().split("\n")[0].split(" ")
    nums = list(map(int, nums))
    
    if nums[0] == -1 and nums[1] == -1 and nums[2] == -1:
        break
    elif nums[0] > 20 or nums[1] > 20 or nums[2] > 20:
        print("w(%d, %d, %d) = %d" % (nums[0], nums[1], nums[2], dp[20][20][20]))
    elif nums[0] <= 0 or nums[1] <= 0 or nums[2] <= 0:
        print("w(%d, %d, %d) = %d" % (nums[0], nums[1], nums[2], dp[0][0][0]))
    else:
        print("w(%d, %d, %d) = %d" % (nums[0], nums[1], nums[2], dp[nums[0]][nums[1]][nums[2]]))
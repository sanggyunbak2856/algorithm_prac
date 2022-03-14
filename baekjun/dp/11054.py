import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split("\n")[0].split(" ")))
dpp = [1] * n
dpm = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[i] < numbers[j]:
            dpp[i] = max(dpp[i], dpp[j] + 1)
        elif numbers[i] > numbers[j]:
            dpm[i] = max(dpp[i], dpp[j] + 1)
            
print(dpp, dpm)
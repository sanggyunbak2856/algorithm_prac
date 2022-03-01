import sys

size = int(sys.stdin.readline())
dp = [0]*(2**(size - 1)) # 경로에 따른 수의 합 저장
triangle = [[] for i in range(size)]

diff = 0
for i in range(size):
    elements = list(map(int , sys.stdin.readline().split('\n')[0].split(" ")))
    triangle[i] = elements

print(triangle)
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split("\n")[0].split(" ")))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split("\n")[0].split(" ")))

for item in mlist:
    if item in nlist:
        print(1)
    else:
        print(0) 
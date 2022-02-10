import sys

numberN = int(sys.stdin.readline())
numberNList = sys.stdin.readline()
numberNList = numberNList.split('\n')[0].split(' ')

numberM = int(sys.stdin.readline())
numberMList = sys.stdin.readline()
numberMList = numberMList.split('\n')[0].split(' ')

for i in numberMList:
    included = False
    for j in numberNList:
        if i == j:
            included = True
    if included:
        print(1)
    else:
        print(0)
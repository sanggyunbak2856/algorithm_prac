import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split("\n ")[0].split(" ")))
nlist.sort()
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split("\n")[0].split(" ")))
answer = [0] * m

def countNum(cardset, findcard, start, end):
    cards = cardset[start:end+1]
    answer = 0
    
    for i in cards:
        if findcard == i:
            answer += 1
    return answer

def solution(cardset, findcard):
    for i in range(len(findcard)):
        start = 0
        end = len(cardset)
        while start < end:
            mid = (start + end) // 2
            
            if cardset[mid] == findcard[i]:
                answer[i] = countNum(cardset, findcard[i], start, end+1)
                break
            elif cardset[mid] < findcard[i]:
                start = mid + 1
            else:
                end = mid - 1

solution(nlist, mlist)
print(answer)
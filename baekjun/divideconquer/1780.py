import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split('\n')[0].split(' '))) for __ in range(n)]
minusone, zero, one = 0, 0, 0
def paperSplit(x, y, size):
    global minusone, zero, one
    standard = paper[x][y]
    if size == 1:
        if standard == 1:
            one += 1
            return
        elif standard == 0:
            zero += 1
            return
        else:
            minusone += 1
            return
    for i in range(x, x + size):
        for j in range(y, y + size):
            if standard != paper[i][j]:
                paperSplit(x, y, size//3)
                paperSplit(x, y + (size//3), size//3)
                paperSplit(x, y + 2 * (size//3), size//3)
                paperSplit(x + (size//3), y, size//3)
                paperSplit(x + (size//3), y + (size//3), size//3)
                paperSplit(x + (size//3), y + 2 * (size//3), size//3)
                paperSplit(x + 2 * (size//3), y, size//3)
                paperSplit(x + 2 * (size//3), y + (size//3), size//3)
                paperSplit(x + 2 * (size//3), y + 2 * (size//3), size//3)
                return
    if standard == -1:
        minusone += 1
        return
    elif standard == 0:
        zero += 1
        return
    elif standard == 1:
        one += 1
        return

paperSplit(0, 0, n)
print(minusone)
print(zero)
print(one)
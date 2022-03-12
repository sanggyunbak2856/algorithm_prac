import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split(" "))) for __ in range(n)]
white, blue = 0, 0

def paperNum(x, y, size):
    color = paper[x][y]
    global white, blue
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != paper[i][j]:
                paperNum(x, y, size//2)
                paperNum(x + (size // 2), y, size//2)
                paperNum(x , y + (size // 2), size//2)
                paperNum(x + (size//2), y + (size//2), size//2)
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return

paperNum(0, 0, n)
print(white)
print(blue)        
    

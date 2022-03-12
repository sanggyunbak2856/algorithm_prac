import sys
n = int(sys.stdin.readline())
video = [list(map(int, sys.stdin.readline().split('\n')[0])) for __ in range(n)]
result = ''

def quadTree(x, y, size):
    global result
    standard = video[x][y]
    
    if size == 1 and standard == 0:
        result += '0'
        return
    elif size == 1 and standard == 1:
        result += '1'
        return
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if standard != video[i][j]:
                result += '('
                quadTree(x, y, size//2)
                quadTree(x, y + (size//2), size//2)
                quadTree(x + (size//2), y, size//2)
                quadTree(x + (size//2), y + (size//2), size//2)
                result += ')'
                return
    if standard == 0:
        result += '0'
        return
    else:
        result += '1'
        return

quadTree(0, 0, n)
print(result)

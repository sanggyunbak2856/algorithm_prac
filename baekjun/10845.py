import sys

number = int(sys.stdin.readline())
queue = list()

for i in range(int(number)):
    command = sys.stdin.readline().split('\n')[0]
    tokenizedCommand = command.split(" ")
    
    if (tokenizedCommand[0] == 'push'):
        insertNum = int(tokenizedCommand[1])
        queue.append(insertNum)
    elif (tokenizedCommand[0] == 'pop'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif (tokenizedCommand[0] == 'size'):
        print(len(queue))
    elif (tokenizedCommand[0] == 'empty'):
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif (tokenizedCommand[0] == 'front'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif (tokenizedCommand[0] == 'back'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
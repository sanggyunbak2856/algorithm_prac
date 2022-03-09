import random

def merge(left, right):
    leftptr, rightptr = 0, 0
    merged = list()
    
    while len(left) > leftptr and len(right) > rightptr:
        if left[leftptr] < right[rightptr]:
            merged.append(left[leftptr])
            leftptr += 1
        else:
            merged.append(right[rightptr])
            rightptr += 1
    
    while len(left) > leftptr:
        merged.append(left[leftptr])
        leftptr += 1
    
    while len(right) > rightptr:
        merged.append(right[rightptr])
        rightptr += 1
    
    return merged
    
def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = data[:medium]
    right = data[medium:]
    return merge(mergesplit(left), mergesplit(right))
    
data = random.sample(range(100), 50)
print(mergesplit(data))

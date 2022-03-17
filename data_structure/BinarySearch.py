def binarySearch(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    elif len(data) == 1 and data[0] != search:
        return False
    elif len(data) == 0:
        return False
    
    print(data)
    medium = len(data) // 2
    if data[medium] == search:
        return True
    elif data[medium] < search:
        return binarySearch(data[medium:], search)
    else:
        return binarySearch(data[:medium], search)

data = [1, 3, 5, 6, 7, 9, 14, 16, 17, 19, 23, 27]

print(binarySearch(data, 9))
print(binarySearch(data, 11))
    
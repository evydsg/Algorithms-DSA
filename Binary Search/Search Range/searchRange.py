def binarySearch(low, high):
    while low <= high:
        mid = (low + high)//2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid

def isCorrect(value):
    if value > 10:
        return 1
    elif value < 10:
        return -1
    else:
        return 0
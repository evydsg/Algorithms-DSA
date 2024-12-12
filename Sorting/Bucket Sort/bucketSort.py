def bucketSort(array):
    counts = [0, 0, 0]

    for color in array:
        counts[color] += 1
    
    index = 0

    for ptrC in range(len(counts)):
        for color in range(counts[ptrC]):
            array[index] = ptrC
            index += 1
    
    return array
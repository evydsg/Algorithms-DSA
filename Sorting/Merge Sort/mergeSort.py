def mergeSort(array, start, end) -> list[array]:

    if end - start + 1 <= 1:
        return array
    
    middle = (start + end) //2

    mergeSort(array, start, middle)
    mergeSort(array, middle + 1, end)
    merge(array, start, middle, end)

    return array

def merge(array, start, middle, end):
    left = array[start: middle + 1]
    right = array[middle + 1: end + 1]

    indexL, indexR, indexA = 0, 0, start
    
    while indexL < len(left) and indexR < len(right):
        if left[indexL] <= right[indexR]:
            array[indexA] = left[indexR]
            indexL += 1
        else:
            array[indexA] = right[indexR]
            indexR += 1
        
        indexA += 1
    
    while indexL < len(left):
        array[indexA] = left[indexL]
        indexA += 1
        indexL += 1
    
    while indexR < len(right):
        array[indexA] = right[indexR]
        indexA += 1
        indexR += 1

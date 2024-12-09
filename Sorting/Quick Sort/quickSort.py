def quickSort(array: list[int], start:int, end: int) -> list[int]:
    if end - start + 1 <= 1:
        return array
    
    pivot = array[end]
    left = start
    
    for index in range(start, end):
        if array[index] < pivot:
            temp = array[left]
            array[left] = array[index]
            array[index] = temp
            left += 1
    
    array[end] = array[left]
    array[left] = pivot

    quickSort(array, start, left - 1)
    quickSort(array, left + 1, end)

    return array
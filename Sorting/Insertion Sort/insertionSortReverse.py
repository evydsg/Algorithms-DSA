def insertionSortReverse(array):
    if len(array) <= 1:
        return array

    for index in range(1, len(array)):
        cur_index = index - 1

        while cur_index >= 0 and array[cur_index + 1] > array[cur_index]:
            array[cur_index + 1], array[cur_index] = array[cur_index], array[cur_index + 1]
            cur_index -= 1
        
    return array

array = [1, 4, 5, 6]
sorted_array = insertionSortReverse(array)

print("Original Array")
for number in array:
    print(number)

print()

print(sorted_array)
for number in sorted_array:
    print(number)
def insertionSort(array):

    for index in range(1, len(array)):
        curr = index - 1

        while curr >= 0 and array[curr + 1] <= array[curr]:
            temp = array[curr+1]
            array[curr + 1] = array[curr]
            array[curr] = temp

            curr -= 1
    
    return array

array = [1,7,9,10,3]
for element in array:
    print(element)

sorted_array = insertionSort(array)

print("Sorted Array")
for element in array:
    print(element)
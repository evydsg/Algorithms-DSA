def insertionSort(array) -> List[array]:

    for index in range(1, len(array)):
        jindex = index - 1

        while jindex >= 0 and array[jindex + 1] < array[jindex]:
            temp = array[jindex + 1]
            array[jindex + 1] = array[jindex]
            array[jindex] = temp
            jindex -= 1
        
        return array
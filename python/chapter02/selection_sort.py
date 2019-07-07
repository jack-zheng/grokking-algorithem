def findSmallest(arr):
    smallest = arr[0]
    index = 0
    for sub in range(1, len(arr)):
        if arr[sub] < smallest:
            smallest = arr[sub]
            index = sub
    return index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        val = findSmallest(arr)
        newArr.append(arr.pop(val))
    return newArr

if __name__ == '__main__':
    import numpy as np
    testArr = np.random.randint(20, size=5)
    print("Test Data: %s" % testArr)
    ret = selectionSort(list(testArr))
    print("Sort result: %s" % ret)
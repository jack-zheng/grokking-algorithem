def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [sub for sub in arr[1:] if sub <= pivot]
        great = [sub for sub in arr[1:] if sub > pivot]
        return quicksort(less) + [pivot] + quicksort(great)

if __name__ == '__main__':
    import numpy as np
    arr = list(np.random.randint(20, size=20))
    print('Test Data: %s' % arr)
    print('Sort result: %s' % quicksort(arr))
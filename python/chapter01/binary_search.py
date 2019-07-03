def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        # this should be more safe
        mid = int(low + (high-low)/2)
        if list[mid] == target:
            return mid
        if list[mid] < target:
            low = mid + 1
        if list[mid] > target:
            high = mid -1
    return -1

if __name__ == '__main__':
    print('Target position: %s' % binary_search(range(100), 43))
    
            
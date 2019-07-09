def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    print('Test arr: %s' % arr)
    print('sum = %s' % sum(arr))
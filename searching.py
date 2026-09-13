def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return print(index)
    return print(-1)

data = [3,4,7,8,9,2,3,5,6,4,7,8]


linear_search(data, 5)
linear_search(data, 100)

def binary_search(arr, target, low, high):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return - 1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    n = len(arr)
    while (i < n) and (arr[i] <= target):
        i *= 2

    low = i // 2
    high = min(i, n - 1)
    return print(binary_search(arr, target, low, high))

data = [10, 20, 30, 40, 50, 60, 70 ,80 ,90, 100, 110, 120, 130, 140, 150, 160, 170, 200, 250]
exponential_search(data, 250)

def quicksortEj2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksortEj2(less) + [pivot] + quicksortEj2(greater)

arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksortEj2(arr))

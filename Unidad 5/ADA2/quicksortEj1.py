def quicksortEj1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortEj1(left) + middle + quicksortEj1(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksortEj1(arr))

def merge_direct_iterative(arr):
    n = len(arr)
    size = 1
    while size < n:
        for left_start in range(0, n, 2 * size):
            mid = min(left_start + size - 1, n - 1)
            right_end = min(left_start + 2 * size - 1, n - 1)
            merge_iterative(arr, left_start, mid, right_end)
        size *= 2
def merge_iterative(arr, left_start, mid, right_end):
    left = arr[left_start:mid + 1]
    right = arr[mid + 1:right_end + 1]
    i = j = 0
    k = left_start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
arr = [38, 27, 43, 3, 9, 82, 10]
merge_direct_iterative(arr)
print("Array ordenado:", arr)


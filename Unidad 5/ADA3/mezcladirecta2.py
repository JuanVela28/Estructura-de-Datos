def merge_direct_in_place(arr):
    n = len(arr)
    size = 1
    while size < n:
        for left_start in range(0, n, 2 * size):
            mid = min(left_start + size - 1, n - 1)
            right_end = min(left_start + 2 * size - 1, n - 1)
            merge_in_place(arr, left_start, mid, right_end)
        size *= 2

def merge_in_place(arr, left_start, mid, right_end):
    left_copy = arr[left_start:mid + 1]
    right_copy = arr[mid + 1:right_end + 1]
    i, j, k = 0, 0, left_start
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_direct_in_place(arr)
print("Array ordenado:", arr)

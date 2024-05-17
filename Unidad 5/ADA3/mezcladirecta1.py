def merge_direct(arr):
    n = len(arr)
    aux = [0] * n
    size = 1
    while size < n:
        for left_start in range(0, n, 2 * size):
            mid = min(left_start + size - 1, n - 1)
            right_end = min(left_start + 2 * size - 1, n - 1)
            merge(arr, aux, left_start, mid, right_end)
        size *= 2

def merge(arr, aux, left_start, mid, right_end):
    i, j, k = left_start, mid + 1, left_start
    while i <= mid and j <= right_end:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1
    while j <= right_end:
        aux[k] = arr[j]
        j += 1
        k += 1
    for i in range(left_start, right_end + 1):
        arr[i] = aux[i]

arr = [38, 27, 43, 3, 9, 82, 10]
merge_direct(arr)
print("Array ordenado:", arr)


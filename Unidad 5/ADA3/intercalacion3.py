def merge_sort_iterative(arr):
    current_size = 1

    while current_size < len(arr):
        left = 0
        while left < len(arr) - current_size:
            mid = min(left + current_size - 1, len(arr) - 1)
            right = min(left + 2 * current_size - 1, len(arr) - 1)
            merge(arr, left, mid, right)
            left += 2 * current_size
        current_size *= 2

def merge(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]

    l = 0
    r = 0
    sorted_index = left

    while l < len(left_copy) and r < len(right_copy):
        if left_copy[l] <= right_copy[r]:
            arr[sorted_index] = left_copy[l]
            l += 1
        else:
            arr[sorted_index] = right_copy[r]
            r += 1
        sorted_index += 1

    while l < len(left_copy):
        arr[sorted_index] = left_copy[l]
        l += 1
        sorted_index += 1

    while r < len(right_copy):
        arr[sorted_index] = right_copy[r]
        r += 1
        sorted_index += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterative(arr)
print("Array ordenado:", arr)

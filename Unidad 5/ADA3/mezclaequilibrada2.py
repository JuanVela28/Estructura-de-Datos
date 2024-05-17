def balanced_merge_sort_in_place(arr):
    if len(arr) <= 1:
        return arr
    third = len(arr) // 3
    left = arr[:third]
    middle = arr[third:2*third]
    right = arr[2*third:]
    balanced_merge_sort_in_place(left)
    balanced_merge_sort_in_place(middle)
    balanced_merge_sort_in_place(right)
    merged = merge_three(left, middle, right)
    arr[:] = merged

def merge_three(left, middle, right):
    result = []
    i = j = k = 0
    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] <= middle[j] and left[i] <= right[k]:
            result.append(left[i])
            i += 1
        elif middle[j] <= left[i] and middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1
    while i < len(left) and j < len(middle):
        if left[i] <= middle[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(middle[j])
            j += 1
    while j < len(middle) and k < len(right):
        if middle[j] <= right[k]:
            result.append(middle[j])
            j += 1
        else:
            result.append(right[k])
            k += 1
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1
    result.extend(left[i:])
    result.extend(middle[j:])
    result.extend(right[k:])
    return result
arr = [38, 27, 43, 3, 9, 82, 10]
balanced_merge_sort_in_place(arr)
print("Array ordenado:", arr)

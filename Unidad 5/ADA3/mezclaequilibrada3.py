def balanced_merge_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    aux = [[] for _ in range(3)]
    for i in range(0, n, 3):
        for j in range(3):
            if i + j < n:
                aux[j].append(arr[i + j])
    sorted_sublists = [sorted(sublist) for sublist in aux]
    return merge_three_iterative(sorted_sublists[0], sorted_sublists[1], sorted_sublists[2])

def merge_three_iterative(left, middle, right):
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
sorted_arr = balanced_merge_sort_iterative(arr)
print("Array ordenado:", sorted_arr)

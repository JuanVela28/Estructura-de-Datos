def shell_sortEj2(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = [5, 2, 8, 9, 1, 3]
shell_sortEj2(arr)
print("Arreglo ordenado:")
print(arr)

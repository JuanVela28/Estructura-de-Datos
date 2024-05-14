def shell_sortEj3(arr):
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

arr = [38, 27, 43, 3, 9, 82, 10]
shell_sortEj3(arr)
print("Arreglo ordenado:")
print(arr)

import heapq

def heapSort(arr):
    return [heapq.heappop(arr) for _ in range(len(arr))]

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Arreglo ordenado:", arr)

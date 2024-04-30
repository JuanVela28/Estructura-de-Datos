def Burbuja1(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print("Lista ordenada usando ordenamiento burbuja (implementación 1):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
Burbuja1(lista.copy())

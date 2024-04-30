def Insercion2(lista):
    for i in range(len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j -= 1
    print("Lista ordenada usando ordenamiento por inserción (implementación 2):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
Insercion2(lista.copy())


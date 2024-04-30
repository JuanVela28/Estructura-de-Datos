def Insercion1(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("Lista ordenada usando ordenamiento por inserción (implementación 1):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
Insercion1(lista.copy())


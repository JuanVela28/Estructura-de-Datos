def PorSeleccion1(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    print("Lista ordenada usando ordenamiento por selección (implementación 1):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
PorSeleccion1(lista.copy())


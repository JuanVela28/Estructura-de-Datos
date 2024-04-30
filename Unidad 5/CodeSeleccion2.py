def PorSeleccion2(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    print("Lista ordenada usando ordenamiento por selección (implementación 2):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
PorSeleccion2(lista.copy())


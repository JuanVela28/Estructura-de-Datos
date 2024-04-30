def Burbuja2(lista):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambio = True
    print("Lista ordenada usando ordenamiento burbuja (implementación 2):", lista)
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
Burbuja2(lista.copy())


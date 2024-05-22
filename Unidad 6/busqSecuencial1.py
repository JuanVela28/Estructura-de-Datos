def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [3, 5, 7, 9, 11, 13]
objetivo = 9
resultado = busqueda_secuencial(lista, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en la posición {resultado}')
else:
    print(f'El número {objetivo} no se encuentra en la lista')

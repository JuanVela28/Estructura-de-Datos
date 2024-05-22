def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista = [3, 5, 7, 9, 11, 13]
objetivo = 9
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en la posición {resultado}')
else:
    print(f'El número {objetivo} no se encuentra en la lista')

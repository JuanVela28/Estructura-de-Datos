def busqueda_binaria_palabras(lista, palabra):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == palabra:
            return medio
        elif lista[medio] < palabra:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista_palabras = ["banana", "cereza", "durazno", "manzana", "mango"]
palabra_buscada = "cereza"
resultado = busqueda_binaria_palabras(lista_palabras, palabra_buscada)

if resultado != -1:
    print(f'La palabra "{palabra_buscada}" se encuentra en la posición {resultado}')
else:
    print(f'La palabra "{palabra_buscada}" no se encuentra en la lista')

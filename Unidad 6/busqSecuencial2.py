def busqueda_secuencial_palabras(lista, palabra):
    for i in range(len(lista)):
        if lista[i] == palabra:
            return i
    return -1

lista_palabras = ["manzana", "banana", "cereza", "durazno", "mango"]
palabra_buscada = "cereza"
resultado = busqueda_secuencial_palabras(lista_palabras, palabra_buscada)

if resultado != -1:
    print(f'La palabra "{palabra_buscada}" se encuentra en la posición {resultado}')
else:
    print(f'La palabra "{palabra_buscada}" no se encuentra en la lista')

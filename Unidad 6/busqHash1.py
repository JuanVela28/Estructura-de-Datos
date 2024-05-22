def buscar_edad(diccionario, nombre):
    return diccionario.get(nombre, "No encontrado")

edades = {
    "Ana": 25,
    "Luis": 30,
    "Marta": 22,
    "Pedro": 35
}
nombre_buscado = "Luis"
resultado = buscar_edad(edades, nombre_buscado)

print(f'La edad de {nombre_buscado} es {resultado}')

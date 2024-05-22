def buscar_capital(diccionario, pais):
    return diccionario.get(pais, "No encontrado")

capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín"
}
pais_buscado = "Italia"
resultado = buscar_capital(capitales, pais_buscado)

print(f'La capital de {pais_buscado} es {resultado}')

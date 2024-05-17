def merge(lista1, lista2):
  lista_fusionada = []
  i = 0
  j = 0
  while i < len(lista1) and j < len(lista2):
    if lista1[i] <= lista2[j]:
      lista_fusionada.append(lista1[i])
      i += 1
    else:
      lista_fusionada.append(lista2[j])
      j += 1
  lista_fusionada += lista1[i:]
  lista_fusionada += lista2[j:]
  return lista_fusionada

def ordenamiento_por_intercalacion(lista):

  if len(lista) <= 1:
    return lista
  medio = len(lista) // 2
  lista_izquierda = ordenamiento_por_intercalacion(lista[:medio])
  lista_derecha = ordenamiento_por_intercalacion(lista[medio:])
  return merge(lista_izquierda, lista_derecha)

lista_desordenada = [5, 2, 4, 6, 1, 3]
lista_ordenada = ordenamiento_por_intercalacion(lista_desordenada)
print(lista_ordenada)

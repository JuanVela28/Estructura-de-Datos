import os

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as file:
        contenido = file.read().strip().split('\n\n')
        registros = []
        for registro in contenido:
            lineas = registro.split('\n')
            nombre = lineas[0].split(': ')[1]
            numero_presentaciones = int(lineas[1].split(': ')[1])
            fechas = lineas[2].split(': ')[1].split(', ')
            registros.append({
                "Nombre": nombre,
                "NumeroPresentaciones": numero_presentaciones,
                "Fechas": fechas
            })
        return registros

def intercalar_archivos(A1, A2, A3):
    i, j, k = 0, 0, 0
    resultado = []

    while i < len(A1) and j < len(A2) and k < len(A3):
        if A1[i]['Nombre'] <= A2[j]['Nombre'] and A1[i]['Nombre'] <= A3[k]['Nombre']:
            resultado.append(A1[i])
            i += 1
        elif A2[j]['Nombre'] <= A1[i]['Nombre'] and A2[j]['Nombre'] <= A3[k]['Nombre']:
            resultado.append(A2[j])
            j += 1
        else:
            resultado.append(A3[k])
            k += 1

    while i < len(A1) and j < len(A2):
        if A1[i]['Nombre'] <= A2[j]['Nombre']:
            resultado.append(A1[i])
            i += 1
        else:
            resultado.append(A2[j])
            j += 1

    while j < len(A2) and k < len(A3):
        if A2[j]['Nombre'] <= A3[k]['Nombre']:
            resultado.append(A2[j])
            j += 1
        else:
            resultado.append(A3[k])
            k += 1

    while i < len(A1) and k < len(A3):
        if A1[i]['Nombre'] <= A3[k]['Nombre']:
            resultado.append(A1[i])
            i += 1
        else:
            resultado.append(A3[k])
            k += 1

    while i < len(A1):
        resultado.append(A1[i])
        i += 1

    while j < len(A2):
        resultado.append(A2[j])
        j += 1

    while k < len(A3):
        resultado.append(A3[k])
        k += 1

    return resultado

def main():
    ruta_base = "D:\\Tecnm\\Tercero\\EstructuraDeDatos\\u5y6\\Examen\\archivos"

    A1 = leer_archivo(os.path.join(ruta_base, 'A1.txt'))
    A2 = leer_archivo(os.path.join(ruta_base, 'A2.txt'))
    A3 = leer_archivo(os.path.join(ruta_base, 'A3.txt'))

    recitales = intercalar_archivos(A1, A2, A3)

    if recitales:
        with open(os.path.join(ruta_base, "RECITALES.txt"), "w") as file:
            for recital in recitales:
                file.write(f"Nombre: {recital['Nombre']}\n")
                file.write(f"Numero de Presentaciones: {recital['NumeroPresentaciones']}\n")
                file.write(f"Fechas de las Presentaciones: {', '.join(recital['Fechas'])}\n")
                file.write("\n")

        print("Archivo RECITALES.txt creado exitosamente.")
    else:
        print("No se encontraron recitales para intercalar.")

if __name__ == "__main__":
    main()
def seleccion_directa_por_nombre(alumnos):
    n = len(alumnos)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if alumnos[j]["nombre"] < alumnos[menor]["nombre"]:
                menor = j
        if menor != i:
            alumnos[i], alumnos[menor] = alumnos[menor], alumnos[i]

def quicksort_por_materias(alumnos):
    if len(alumnos) <= 1:
        return alumnos
    pivote = alumnos.pop()
    menores = []
    mayores = []
    for alumno in alumnos:
        if alumno["materias_aprobadas"] <= pivote["materias_aprobadas"]:
            menores.append(alumno)
        else:
            mayores.append(alumno)
    return quicksort_por_materias(menores) + [pivote] + quicksort_por_materias(mayores)

def main():
    alumnos = [
        {"nombre": "Angie", "matricula": "E22080712", "materias_aprobadas": 7, "promedio": 8.5 },
        {"nombre": "Luis", "matricula": "E23080244", "materias_aprobadas": 7, "promedio": 9 },
        {"nombre": "Pablo", "matricula": "E23090823", "materias_aprobadas": 5 , "promedio": 6.8 },
        {"nombre": "Marco", "matricula": "E23098923", "materias_aprobadas": 6 , "promedio": 8.7 },
        {"nombre": "Alejandro", "matricula": "E23090823", "materias_aprobadas": 6 , "promedio": 7.9 },
        {"nombre": "Quijano", "matricula": "E239987", "materias_aprobadas": 7, "promedio": 9 },
        {"nombre": "Mauricio", "matricula": "E23090876", "materias_aprobadas": 7, "promedio": 9.8 },
        {"nombre": "David", "matricula": "E22980867", "materias_aprobadas": 6, "promedio": 8.6 },
        {"nombre": "Jesús", "matricula": "E22090863", "materias_aprobadas": 5, "promedio": 6.4 },
        {"nombre": "Antonio", "matricula": "E21334809", "materias_aprobadas": 5, "promedio": 6.2 },
        {"nombre": "Toñito", "matricula": "E20208076", "materias_aprobadas": 6, "promedio": 8.1 },
        {"nombre": "Javi", "matricula": "E20206789", "materias_aprobadas": 7, "promedio": 8.7 },
        {"nombre": "Daniel", "matricula": "E23878809", "materias_aprobadas": 8, "promedio": 10 },
        {"nombre": "Diego", "matricula": "E23445566", "materias_aprobadas": 6, "promedio": 7.8 },
        {"nombre": "Ader", "matricula": "E20223344", "materias_aprobadas": 7, "promedio": 8.2 },
        {"nombre": "Tapia", "matricula": "E19223344", "materias_aprobadas": 7, "promedio": 8 },
        {"nombre": "Gerardo", "matricula": "E20665543", "materias_aprobadas": 7 , "promedio": 7.2 },
        {"nombre": "Isaac", "matricula": "E23448823", "materias_aprobadas": 6, "promedio": 7 },
        {"nombre": "Kevin", "matricula": "E20894737", "materias_aprobadas": 5, "promedio": 6.1 },
        {"nombre": "Sami", "matricula": "E17382840", "materias_aprobadas": 7, "promedio": 7.6 }
    ]

    print("Alumnos antes de ordenar:")
    for alumno in alumnos:
        print(alumno)

    seleccion_directa_por_nombre(alumnos)
    print("\nAlumnos ordenados por nombre:")
    for alumno in alumnos:
        print(alumno)

    alumnos_ordenados_por_materias = quicksort_por_materias(alumnos.copy())
    print("\nAlumnos ordenados por número de materias aprobadas:")
    for alumno in alumnos_ordenados_por_materias:
        print(alumno)

if __name__ == "__main__":
    main()

postres = [
    {"nombre": "Brownie", "ingredientes": ["Chocolate", "Cacao en polvo", "Huevos", "Azúcar", "Mantequilla", "Esencia de vainilla", "Harina"]},
    {"nombre": "Cheesecake de fresa", "ingredientes": ["Galletas", "Mantequilla", "Limón", "Leche condensada", "Crema para batir", "Esencia de vainilla", "Fresas", "Azúcar"]},
    {"nombre": "Gelato Cookies & Cream", "ingredientes": ["Crema para batir", "Leche condensada", "Esencia de vainilla", "Galleta oreo "]},
    {"nombre": "Pie de limón", "ingredientes": ["Mantequilla", "Harina", "Huevo", "Leches condensada", "Esencia de vainilla", "Jugo de limón", "Azúcar", "Azúcar flor"]},
    {"nombre": "Queso napolitano", "ingredientes": ["Leche condensada", "Leche evaporada", "Yemas de huevo", "Azúcar", "Vainilla"]},
]

def mostrar_postres_con_ingredientes():
    for indx, postre in enumerate(postres, 1):
        print(f"{indx}. {postre['nombre']} - Ingredientes: {', '.join(postre['ingredientes'])}")

def agregar_ingredientes():
    mostrar_postres_con_ingredientes()
    opcion = int(input("Seleccione el número del postre al que desea agregar ingredientes: "))
    postre = postres[opcion - 1]
    ingredientes = input("Ingrese los ingredientes a agregar separados por coma: ").split(",")
    postre['ingredientes'].extend(ingredientes)
    print("Ingredientes agregados correctamente.")

def eliminar_ingredientes():
    mostrar_postres_con_ingredientes()
    opcion = int(input("Seleccione el número del postre al que desea eliminar ingredientes: "))
    postre = postres[opcion - 1]
    print(f"Ingredientes del {postre['nombre']}: {postre['ingredientes']}")
    ingredientes_a_eliminar = input("Ingrese los ingredientes a eliminar separados por coma: ").split(",")
    for ingrediente in ingredientes_a_eliminar:
        if ingrediente in postre['ingredientes']:
            postre['ingredientes'].remove(ingrediente)
    print("Ingredientes eliminados correctamente.")

def ingresar_nuevo_postre():
    nombre = input("Ingrese el nombre del nuevo postre: ")
    ingredientes = input("Ingrese los ingredientes del nuevo postre separados por coma: ").split(",")
    postres.append({"nombre": nombre, "ingredientes": ingredientes})
    print("Nuevo postre agregado correctamente.")

def eliminar_postre():
    mostrar_postres_con_ingredientes()
    opcion = int(input("Seleccione el número del postre que desea eliminar: "))
    del postres[opcion - 1]
    print("Postre eliminado correctamente.")

while True:
    print("---------Menú Principal---------")
    print("1. Mostrar postres con ingredientes")
    print("2. Agregar ingredientes a un postre")
    print("3. Eliminar ingredientes de un postre")
    print("4. Ingresar un nuevo postre con sus ingredientes")
    print("5. Eliminar un postre con sus ingredientes")
    print("6. Salir")

    option = input("Ingrese una opción de la lista: ")
    if option == "1":
        mostrar_postres_con_ingredientes()
    elif option == "2":
        agregar_ingredientes()
    elif option == "3":
        eliminar_ingredientes()
    elif option == "4":
        ingresar_nuevo_postre()
    elif option == "5":
        eliminar_postre()
    elif option == "6":
        print("Está saliendo del programa.")
        break
    else:
        print("Opción inválida. Seleccione una opción válida de la lista.")

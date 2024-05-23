import sys
import ejercicio4   
import ejercicio1

def mostrar_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Intercalar archivos y formar RECITALES")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        print("Ejecutando Opción 1...")
        ejercicio1.main()
    elif opcion == '2':
        print("Ejecutando Opción 2...")

    elif opcion == '3':
        print("Ejecutando Opción 3...")
        
    elif opcion == '4':
        print("Intercalando archivos y formando RECITALES...")
        ejercicio4.main()
    elif opcion == '5':
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion)

class Hotel:
    def __init__(self, nombre, ciudad, estrellas, cuartos):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estrellas = estrellas
        self.cuartos = cuartos

    def __repr__(self):
        return f"Hotel(Nombre: '{self.nombre}', Ciudad: '{self.ciudad}', Estrellas: {self.estrellas}, Cuartos: {self.cuartos})"

def intercambiar(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def particion(arr, bajo, alto):
    pivote = arr[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if (arr[j].ciudad, arr[j].nombre) < (pivote.ciudad, pivote.nombre):
            i += 1
            intercambiar(arr, i, j)
    intercambiar(arr, i + 1, alto)
    return i + 1

def quicksort(arr, bajo, alto):
    if bajo < alto:
        pi = particion(arr, bajo, alto)
        quicksort(arr, bajo, pi - 1)
        quicksort(arr, pi + 1, alto)

def main():
    hoteles = [
        Hotel("Hotel Del Gobernador", "Mérida", 4.2, 92),
        Hotel("Holiday Inn Coatzacoalcos", "Coatzacoalcos", 4.3, 120),
        Hotel("Gran Real Yucatán", "Mérida", 4.0, 73),
        Hotel("Hotel Terraza Del Sol", "Coatzacoalcos", 3.8, 55),
        Hotel("City Express Apizaco", "Apizaco", 4.4, 104),
    ]

    quicksort(hoteles, 0, len(hoteles) - 1)

    for hotel in hoteles:
        print(hotel)

if __name__ == "__main__":
    main()

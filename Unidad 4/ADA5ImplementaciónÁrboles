class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def obtener_raiz(self):
        return self.raiz.valor

    def obtener_numero_de_ramas(self):
        return self.contar_ramas(self.raiz)

    def obtener_numero_de_niveles(self):
        return self.contar_niveles(self.raiz)

    def obtener_tipo(self):
        tipo = self.verificar_tipo(self.raiz)
        return tipo

    def contar_ramas(self, nodo):
        if not nodo.hijos:
            return 0
        else:
            ramas = len(nodo.hijos)
            for hijo in nodo.hijos:
                ramas += self.contar_ramas(hijo)
            return ramas

    def contar_niveles(self, nodo):
        if not nodo.hijos:
            return 1
        else:
            niveles = []
            for hijo in nodo.hijos:
                niveles.append(1 + self.contar_niveles(hijo))
            return max(niveles)

    def verificar_tipo(self, nodo):
        if not nodo.hijos:
            return "Hoja"
        else:
            tipo = "Interior"
            for hijo in nodo.hijos:
                tipo_hijo = self.verificar_tipo(hijo)
                if tipo_hijo == "Hoja":
                    tipo = "Mixto"
                    break
            return tipo

    def mostrar_informacion(self):
        print("Raíz del árbol:", self.obtener_raiz())
        print("Número de ramas del árbol:", self.obtener_numero_de_ramas())
        print("Número de niveles del árbol:", self.obtener_numero_de_niveles())
        print("Tipo del árbol:", self.obtener_tipo())

if __name__ == "__main__":
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)

    nodo1.hijos = [nodo2, nodo3]
    nodo2.hijos = [nodo4, nodo5]
    nodo3.hijos = [nodo6, nodo7]

    arbol = Arbol(nodo1)
    arbol.mostrar_informacion()

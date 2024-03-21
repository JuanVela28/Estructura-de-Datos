from abc import ABC, abstractmethod

class Pedido:
    def __init__(self, cantProducto, cliente):
        self.cliente = cliente
        self.cantProducto = cantProducto

    def __str__(self):
        return f"     Customer: {self.cliente}\n     Quantity: {self.cantProducto}\n     ----------------------------------"

class InterfazCola(ABC):
    @abstractmethod
    def colaSize(self):
        pass

    @abstractmethod
    def emptyCola(self):
        pass

    @abstractmethod
    def frente(self):
        pass

    @abstractmethod
    def sumarP(self, informacion):
        pass

    @abstractmethod
    def restarP(self):
        pass

class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

    def nextProduct(self):
        return self.siguiente

class Cola(InterfazCola):
    def __init__(self):
        self.frente = self.final = None

    def emptyCola(self):
        return self.frente is None

    def colaSize(self):
        contador = 0
        temp = self.frente
        while temp:
            contador += 1
            temp = temp.nextProduct()
        return contador

    def sumarP(self, informacion):
        nodo = Nodo(informacion)

        if self.final is None:
            self.frente = self.final = nodo
            return
        self.final.siguiente = nodo
        self.final = nodo

    def restarP(self):
        if self.emptyCola():
            return None
        temp = self.frente
        self.frente = temp.obtener_siguiente()

        if self.frente is None:
            self.final = None
        return temp.dato

    def frente(self):
        if self.emptyCola():
            return None
        return self.frente.dato

    def cola(self):
        nodo = self.frente
        print("************** QUEUE DUMP **************")
        print(f"   Size: {self.colaSize()}")
        contador = 0
        while nodo:
            contador += 1
            print(f"   ** Element {contador}")
            print(nodo.dato)
            nodo = nodo.nextProduct()
        print("***************************************")

pedidoEmpresa = Cola()
pedidoEmpresa.sumarP(Pedido(20, "Cliente #1"))
pedidoEmpresa.sumarP(Pedido(30, "Cliente #2"))
pedidoEmpresa.sumarP(Pedido(40, "Cliente #3"))
pedidoEmpresa.sumarP(Pedido(50, "Cliente #4"))
pedidoEmpresa.cola()

class ManejadorListas:
    def __init__(self, lista) -> None:
        self.lista = lista

    def obtenerPares(self):
        pares = []
        for num in self.lista:
            if num % 2 == 0:
                pares.append(num)
        return pares

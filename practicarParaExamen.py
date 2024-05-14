class Division:
    def __init__(self, num1:int, num2:int) -> None:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Ambos números deben ser enteros.")
        self.num1 = num1
        self.num2 = num2

    def dividir(self):
        try:
            resultado = self.num1 / self.num2
            return resultado
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")

if __name__ == "__main__": 
    objeto = Division(1, 5)
    print(objeto.dividir())
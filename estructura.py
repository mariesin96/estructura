class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.p1 = 3.1415

    def calcularPerimetro(self):
        return 2 * self.p1 * self.radio

    def calcularArea(self):
        return self.p1 * self.radio ** 2

    def getPi(self):
        return self.p1

    def setRadio(self, nuevoValor):
        if isinstance(nuevoValor, (int, float)):
            if nuevoValor > 0:
                self.radio = nuevoValor
                print(f"El radio se ha modificado correctamente: {self.radio}")
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un número positivo")


# Crear una instancia del círculo y ejecutar los cálculos
c1 = Circulo(2.5)
print("Área:", c1.calcularArea())
print("Perímetro:", c1.calcularPerimetro())
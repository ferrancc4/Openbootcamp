class Vehiculo:
    _color = ""
    _ruedas = 0
    _puertas = 0

    def __init__(self):
        self.queColor("Rojo")
        self.numRuedas(4)
        self.numPuertas(5)

    def __str__(self):
        return "Color: {}\n{} ruedas\n{} puertas".format(self._color, self._ruedas, self._puertas)

    def queColor(self, colorito):
        self._color = colorito

    def numRuedas(self, rueditas):
        self._ruedas = rueditas

    def numPuertas(self, puerta):
        self._puertas = puerta


class Coche(Vehiculo):
    _velocidad = 0
    _cilindrada = 0

    def __init__(self):
        super().__init__()
        self.velMax(120)
        self.caballos(200)

    def __str__(self):
        return super().__str__() + "\nVelocidad màxima {}\nCilindrada {}".format(self._velocidad, self._cilindrada)

    def velMax(self, vel):
        self._velocidad = vel

    def caballos(self, cv):
        self._cilindrada = cv



coche1 = Coche()

print(coche1)

print("\nUsando constructores\n")
print("El cochce es de color:", coche1._color)
print("El coche tiene:", coche1._ruedas, "ruedas")
print("El coche tiene:", coche1._puertas, "puertas")
print("La velocidad máxima es:", coche1._velocidad)
print("El coche tiene:", coche1._cilindrada, "caballos")

print(coche1)

print("\nUsando metodos\n")

coche1.queColor("verde")
coche1.numRuedas(4)
coche1.numPuertas(3)
coche1.velMax(200)
coche1.caballos(500)

print("El cochce es de color:", coche1._color)
print("El coche tiene:", coche1._ruedas, "ruedas")
print("El coche tiene:", coche1._puertas, "puertas")
print("La velocidad máxima es:", coche1._velocidad)
print("El coche tiene:", coche1._cilindrada, "caballos")

print(coche1)
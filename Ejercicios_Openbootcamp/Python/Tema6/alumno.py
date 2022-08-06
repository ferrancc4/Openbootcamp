
class Alumno ():
    _nombre = None
    _nota = 0

    def comoSeLlama (self, nombre):
        self._nombre = nombre

    def suNota (self, nota):
        self._nota = nota

    def resultados(self):
        if self._nota >= 5:
            print("El alumno", self._nombre, "esta aprobado con una nota de", self._nota)
        else:
            print("El alumno", self._nombre, "esta suspendido con una nota de", self._nota)

Juan = Alumno()

Juan.comoSeLlama("Juan")
Juan.suNota(7)
Juan.resultados()


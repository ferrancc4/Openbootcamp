import math

def areaTriangulo (base, altura):
    
    return ((int(base) * int(altura))/2)

def areaCirculo (radio):
    return round(math.pi * math.pow(int(radio), 2), 2)

print("Calculo area de un triangulo")
baseTriangulo = input("Cuanto mide la base?")
alturaTriangulo = input("Cuanto mide la altura?")
print("El area del triangulo con base ", baseTriangulo, " y altura ", alturaTriangulo, " es de ", areaTriangulo(baseTriangulo, alturaTriangulo))
print()
print("Calculo area de un circulo")
radioCirculo = input("Cuanto mide el radio?")
print("El area del circulo con radio ", radioCirculo, " es de ", areaCirculo(radioCirculo))


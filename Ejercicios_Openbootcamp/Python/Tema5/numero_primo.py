
def numeroPrimo (numero):
    for i in range(2, numero - 1):
        if (numero % i) == 0:
            return False
    return True

primo = input("Número entero = ")
respuesta = numeroPrimo(int(primo))

if respuesta:
    print(primo, " es un número primo")
else:
    print(primo, " no es un numero primo")


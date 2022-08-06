import Calculadora as c


def main():
    numero1 = input("Número 1: ")
    numero2 = input("Número 2: ")
    print("\nLa suma de", numero1, "más", numero2, "es:", c.suma(int(numero1), int(numero2)))
    print("La resta de", numero1, "menos", numero2, "es:", c.resta(int(numero1), int(numero2)))
    print("La multiplicación de", numero1, "por", numero2, "es:", c.mitiplicacion(int(numero1), int(numero2)))
    print("La división de", numero1, "por", numero2, "es:", c.division(int(numero1), int(numero2)))


if __name__ == "__main__":
    main()


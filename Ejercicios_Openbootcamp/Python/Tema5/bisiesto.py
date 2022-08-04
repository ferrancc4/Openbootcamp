
# un año es bisiesto si:
#   - es multiplo de 4
#   - no es multiplo de 100 pero si es multiplo de 400

def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

ano = input("Este año es bisiesto? ")

resultado = bisiesto(int(ano))

if resultado:
    print("Es bisiesto")
else:
    print("No es bisiesto")


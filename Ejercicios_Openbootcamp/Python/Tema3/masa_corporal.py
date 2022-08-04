import math

peso = float(input('¿Cual es tu peso? (en kg)'))
estatura = float(input('¿Cuanto mides? (en m)'))

imc = round(peso/math.pow(estatura, 2), 2)

print ('Tu IMC es de ' + str(imc))


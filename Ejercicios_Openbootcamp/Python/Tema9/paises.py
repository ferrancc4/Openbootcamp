
valores = input('Agregar paises una lista separados por comas y un espacio después la coma\n¿Cual es la lista de '
                'paises? ')

# Ponemos todos los paises con la primera letra en mayúscula,
# separamos la string por la coma y la ordenamos alfabéticamente

paises = sorted(set(valores.title().split(', ')))

print('Los paises son:\n    ', paises)


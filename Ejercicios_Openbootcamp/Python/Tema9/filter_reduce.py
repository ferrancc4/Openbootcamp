from functools import reduce


def operacionesLista(lista):
    resfilter = list(filter(lambda x: x % 2, lista))
    print('Lista de impares: ', resfilter)

    resreduce = reduce(lambda a, b: a + b, list(resfilter))

    print('Lista reducida: ', resreduce)


valor1 = int(input('Valor inicial de la lista: '))
valor2 = int(input('Valor final de la lista: '))
print('Lista inicial: ', list(range(valor1, valor2 + 1)))

operacionesLista(list(range(valor1, valor2 + 1)))


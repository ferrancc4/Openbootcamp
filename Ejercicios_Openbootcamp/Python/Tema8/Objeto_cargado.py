import pickle

class Vehiculo:

    def __init__(self, tipo, sonido):
        self.tipo = tipo
        self.sonido = sonido

coche1 = Vehiculo('coche', 'burrum')

f = open('coche1', 'wb')
pickle.dump(coche1, f)
f.close()

# si queremos un coche igual lo podemos cargar
f = open('coche1', 'rb')
coche2 = pickle.load(f)
f.close()

print(coche2.tipo)
print(coche2.sonido)


f = open('mifichero.txt', 'w')
f.write('Primera vez que escribo\n')
f.close()

f = open('mifichero.txt', 'r+')
f.readline()
f.write('Segunda vez\n')

f.seek(0)
print(f.read())
f.close()


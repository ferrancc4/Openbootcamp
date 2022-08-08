import tkinter
from tkinter import ttk  # toolkit per ficar estil
import random

window_pack = tkinter.Tk()
window_pack.title('Geometria Pack')

window_grid = tkinter.Tk()
window_grid.title('Geometria Grid')

window_place = tkinter.Tk()
window_place.title('Geometria Place')

# Geometria pack per ficar coses tipo llista tant horitzontal com vertical

label1 = tkinter.Label(window_pack, text="label1", bg="yellow", fg="blue")
label1.pack(ipadx=45, ipady=15, fill='x')

label2 = tkinter.Label(window_pack, text="label2", bg="purple", fg="white")
label2.pack(ipadx=45, ipady=15, fill='x')

label3 = tkinter.Label(window_pack, text="label3", bg="blue", fg="white")
label3.pack(ipadx=45, ipady=15, fill='x')

label4 = tkinter.Label(window_pack, text="label4", bg="red", fg="white")
label4.pack(ipadx=15, ipady=15, side='left')

label5 = tkinter.Label(window_pack, text="label5", bg="yellow", fg="black")
label5.pack(ipadx=15, ipady=15, side='left')

label6 = tkinter.Label(window_pack, text="label6", bg="green", fg="white")
label6.pack(ipadx=15, ipady=15, side='right')

# Geometria tipus grid és com tenir una malla tipus un excel
# columna0   columna1   columna3
# (0,0)      (1,0)      (2,0)  fila 0
# (0,1)      (1,1)      (2,1)  fila 1
# (0,2)      (1,2)      (2,2)  fila 2
# (0,3)      (1,3)      (2,3)  fila 3

window_grid.columnconfigure(0, weight=1)
window_grid.columnconfigure(0, weight=3)

## USUARI
# Etiqueta usuari
username_label = ttk.Label(window_grid, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)  # sticky fixa la label

# Camp usuari
username_entry = ttk.Entry(window_grid)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

## PASSWORD
# Etiqueta password
password_label = ttk.Label(window_grid, text='Password:')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)  # sticky fixa la label

# Camp password
password_entry = ttk.Entry(window_grid, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

## BOTON
login_button = ttk.Button(window_grid, text='Login')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

# Geometria place per posicionar un element de forma absoluta a la finestra o relativa a un altre element amb una x o y

colores = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

for x in range(0, 10):
    color = random.randint(0, len(colores)-1)
    color2 = random.randint(0, len(colores)-1)
    label = tkinter.Label(window_place, text="Etiqueta!", bg=colores[color], fg=colores[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

window_pack.mainloop()
window_grid.mainloop()
window_place.mainloop()

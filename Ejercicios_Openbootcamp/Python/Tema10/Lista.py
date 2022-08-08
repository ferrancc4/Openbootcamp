import tkinter as tk

window = tk.Tk()
window.title('Lista seleccionable')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

tk.Label(window, text="Selecciona colores").grid(column=0, row=0, sticky=tk.W)

lista = ['Azul', 'Rojo', 'Verde', 'Blanco', 'Negro']
lista_items = tk.StringVar(value=lista)
tk.Listbox(window, height=5, listvariable=lista_items).grid(column=1, row=0, sticky=tk.E)

window.mainloop()


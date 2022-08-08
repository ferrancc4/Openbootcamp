import tkinter as tk

# Función seleccionada

def seleccionar():
    Color_favorito.config(text=f'Tu color favorito es: {color.get()}')


# Función reiniciar
def reiniciar():
    color.set(None)
    Color_favorito.config(text="")

# Creación ventana
window = tk.Tk()



# Label
label1 = tk.Label(window, text="Elige tu color favorito:")
label1.pack()

# RadioButtons

color = tk.StringVar()
color.set("")

tk.Radiobutton(window, text="Azul", variable=color,
            value='Azul', command=seleccionar).pack()
tk.Radiobutton(window, text="Amarillo", variable=color,
            value='Amarillo', command=seleccionar).pack()
tk.Radiobutton(window, text="Rojo", variable=color,
            value='Rojo', command=seleccionar).pack()
tk.Radiobutton(window, text="Blanco", variable=color,
            value='Blanco', command=seleccionar).pack()
tk.Radiobutton(window, text="Negro", variable=color,
            value='Negro', command=seleccionar).pack()

Color_favorito = tk.Label(window, text="")
Color_favorito.pack()

Boton_reiniciar = tk.Button(window, text="Reiniciar", command=reiniciar)
Boton_reiniciar.pack()

window.mainloop()

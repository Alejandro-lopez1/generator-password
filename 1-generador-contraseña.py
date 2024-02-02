import tkinter as tk 
from tkinter import Entry, Button, Label, StringVar
import random
import string

class GeneradorContrasena:
    def __init__(self, root):
        self.root = root
        self.root.title ('Generador de Contraseñas')

        self.longitud_var = StringVar()
        self.contrasena_var = StringVar()

        #Etiqueta y entrada para la longitud de la contraseña
        Label(root, text='Longitud de la Contraseña:').grid(row=0, column=0, padx=10, pady=10)
        Entry(root, textvariable=self.longitud_var).grid(row=0, column=1, padx=10, pady=10)

        #botón para generar la contraseña
        Button(root, text='Generar Contraseña', command=self.generar_contrasena).grid(row=1, column=0, columnspan=2, pady=10)

        #etiqueta para mostrar la contraseña generada
        Label(root, text='Contraseña Generada:').grid(row=2, column=0, padx=10, pady=10)
        Entry(root, textvariable=self.contrasena_var, state='readonly').grid(row=2, column=1, padx=10, pady=10)

    def generar_contrasena(self):
        try:
            longitud_deseada = int(self.longitud_var.get())
            if longitud_deseada > 0:
                caracteres = string.ascii_letters + string.digits + string.punctuation
                nueva_contrasena = ''.join(random.choice(caracteres) for _ in range(longitud_deseada))
                self.contrasena_var.set(nueva_contrasena)
            else:
                self.contrasena_var.set('Error: Longitud no válida')
        except ValueError:
            self.contrasena_var.set('Error: Longitud no válida')

if __name__ == '__main__':
    root = tk.Tk()
    app = GeneradorContrasena(root)
    root.mainloop()
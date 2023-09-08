import tkinter as tk

def mostrar_estado():
    estado = checkbox_var.get()
    if estado == 1:
        etiqueta_estado.config(text="La casilla está marcada")
    else:
        etiqueta_estado.config(text="La casilla no está marcada")

ventana_principal = tk.Tk()
ventana_principal.title("Casilla de Verificación")
ventana_principal.geometry("400x300")

# Variable de control para la casilla de verificación
checkbox_var = tk.IntVar()

# Crear la casilla de verificación con el texto antes del checkbox
casilla_verificacion = tk.Checkbutton(ventana_principal, variable=checkbox_var, text="Casilla de Verificación", anchor="w", command=mostrar_estado)
casilla_verificacion.pack()

etiqueta_estado = tk.Label(ventana_principal, text="")
etiqueta_estado.pack()

ventana_principal.mainloop()

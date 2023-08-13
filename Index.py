import tkinter as tk
from tkinter import font

root = tk.Tk()

# Obtener una lista de todas las fuentes disponibles
all_fonts = font.families()

# Crear un widget Label para mostrar la lista de fuentes
font_list_label = tk.Label(root, text="\n".join(all_fonts), font=("Arial", 12))
font_list_label.pack()

root.mainloop()

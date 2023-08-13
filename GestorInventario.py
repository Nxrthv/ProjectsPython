import tkinter as tk
import xlsxwriter
from tkinter import messagebox
from tkinter import ttk

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario")
        root.geometry("450x150")
        icono = tk.PhotoImage(file="Inventario.png")
        root.iconphoto(True, icono)

        self.inventario = {}

        self.label_nombre = tk.Label(root, text="Producto:", font=("Microsoft Tai Le", 14))
        self.label_nombre.place(x=30,y=20)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.place(x=130,y=25)

        self.label_cantidad = tk.Label(root, text="Cantidad:", font=("Microsoft Tai Le", 14))
        self.label_cantidad.place(x=30,y=60)

        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.place(x=130,y=65)

        self.boton_agregar = ttk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.boton_agregar.place(x=280,y=20)

        self.boton_mostrar = ttk.Button(root, text="Mostrar Inventario", command=self.mostrar_inventario)
        self.boton_mostrar.place(x=280,y=65)

    def agregar_producto(self):
        """nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()

        if nombre and cantidad:
            self.inventario[nombre] = int(cantidad)
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado al inventario.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el nombre y la cantidad del producto.")

        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)"""

        archivo = xlsxwriter.workbook('Inventario.xlsx')
        hoja=archivo.add_worksheet()
        productos = [self.label_nombre, self.label_cantidad]

        for i in range(len(productos)):
            hoja.write(0,i)
        archivo.close()

    def mostrar_inventario(self):
        if not self.inventario:
            messagebox.showinfo("Inventario Vacío", "El inventario está vacío.")
        else:
            mensaje = "Inventario:\n"
            for producto, cantidad in self.inventario.items():
                mensaje += f"{producto}: {cantidad}\n"
            messagebox.showinfo("Inventario", mensaje)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
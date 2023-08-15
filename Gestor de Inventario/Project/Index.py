import tkinter as tk
from tkinter import ttk
from Model.Inventario_dao import Crear_Tabla, Borrar_Tabla

#Hereda de tk.Frame
class Funciones(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()

        #Llama a las Funciones
        self.Menu()
        self.Campos()
        self.Botones()
        self.Tabla()

    #Contenido
    def Menu(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
        menu_inicio.add_command(label='Crear un Registro en DB', command=Crear_Tabla)
        menu_inicio.add_command(label='Eliminar Registro en DB', command=Borrar_Tabla)
        menu_inicio.add_command(label='Salir', command=self.root.destroy)

        menu_configuracion = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label='Configuracion', menu=menu_configuracion)
        menu_configuracion.add_command(label='Ayuda')

    #Campos
    def Campos(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row= 0 , column = 1, columnspan = 2)

        self.label_precio = tk.Label(self, text ='Precio: ')
        self.label_precio.config(font = ('Arial', 12, 'bold'))
        self.label_precio.grid(row = 1,column = 0, padx = 10, pady = 10)

        self.precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.precio)
        self.entry_precio.config(width = 50, font = ('Arial', 12))
        self.entry_precio.grid(row= 1 , column = 1, columnspan = 2)

        self.label_disponible = tk.Label(self, text ='Disponible: ')
        self.label_disponible.config(font = ('Arial', 12, 'bold'))
        self.label_disponible.grid(row = 2,column = 0, padx = 10, pady = 10)

        self.disponible = tk.StringVar()
        self.entry_disponible = tk.Entry(self, textvariable=self.disponible)
        self.entry_disponible.config(width = 50, font = ('Arial', 12))
        self.entry_disponible.grid(row= 2 , column = 1, columnspan = 2)

    #Botones
    def Botones(self):
        self.btn_nuevo = tk.Button(self, text="Nuevo", command=self.Habilitar)
        self.btn_nuevo.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#158645', cursor = 'hand2', activebackground = '#35bd6f')
        self.btn_nuevo.grid(row = 3, column = 0, padx = 20, pady = 20)

        self.btn_guardar = tk.Button(self, text="Guardar", command=self.Guardar)
        self.btn_guardar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#1658a2', cursor = 'hand2', activebackground = '#3586df')
        self.btn_guardar.grid(row = 3, column = 1, padx = 20, pady = 20)

        self.btn_cancelar = tk.Button(self, text="Cancelar", command=self.Desabilitar)
        self.btn_cancelar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#bd152e', cursor = 'hand2', activebackground = '#e15370')
        self.btn_cancelar.grid(row = 3, column = 2, padx = 20, pady = 20)

    #Habilitar y Desabilitar los Campos
    """def Hab_Des(self):
        Estado = self.btn_nuevo['disabled']

        if Estado == tk.NrORMAL:
            self.btn_guardar.config(state=tk.DISABLED)
            self.btn_cancelar.config(state=tk.DISABLED)
        else:
            self.btn_guardar.config(state=tk.NORMAL)
            self.btn_cancelar.config(state=tk.NORMAL)"""
    def Habilitar(self):
        self.entry_nombre.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_disponible.config(state='normal')

        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
            
    def Desabilitar(self):
        self.nombre.set('')
        self.precio.set('')
        self.disponible.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_disponible.config(state='disabled')

        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')

    def Guardar(self):
        self.Desabilitar()

    #Tabla
    def Tabla(self):
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Precio', 'Disponible'))
        self.tabla.grid(row=4, column=0, columnspan=4)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Precio')
        self.tabla.heading('#3', text='Disponible')

        self.tabla.insert('',0,text='1', values=('Cargador', '35', '6'))

        #Boton Editar
        self.btn_editar = tk.Button(self, text="Editar")
        self.btn_editar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#158645', cursor = 'hand2', activebackground = '#35bd6f')
        self.btn_editar.grid(row = 5, column = 0, padx = 20, pady = 20)

        #Boton Eliminar
        self.btn_eliminar = tk.Button(self, text="Eliminar")
        self.btn_eliminar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#bd152e', cursor = 'hand2', activebackground = '#e15370')
        self.btn_eliminar.grid(row = 5, column = 1, padx = 20, pady = 20)

    #Configuracion de la Ventana
def main():
    root = tk.Tk()
    root.title('Inventario')
    icono = tk.PhotoImage(file="Img/Inventario.png")
    root.iconphoto(True, icono)
    root.geometry("750x400")

    root = Funciones(root)

    root.mainloop()

if __name__ == '__main__':
    main()
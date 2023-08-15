import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Inventario')
    icono = tk.PhotoImage(file="Img/Inventario.png")
    root.iconphoto(True, icono)
    root.geometry("750x400")

    root = Funciones(root = root)

    """Finalizador"""
    root.mainloop()

class Funciones:

    #Contenido de la Ventana
    def Contenido(root):
    #Menu
        barra_menu = tk.Menu(root)
        root.config(menu = barra_menu)

        menu_inicio = tk.Menu(barra_menu, tearoff = 0)
        barra_menu.add_cascade(label ='Inicio', menu = menu_inicio)
        menu_inicio.add_command(label ='Crear un Registro en DB')
        menu_inicio.add_command(label ='Eliminar Registro en DB')
        menu_inicio.add_command(label ='Salir', command = root.destroy)

        menu_configuracion = tk.Menu(barra_menu, tearoff = 0)
        barra_menu.add_cascade(label='Configuracion', menu = menu_configuracion)
        menu_configuracion.add_command(label='Ayuda')

    #Campos
    def Campos(self):
        self.label_nombre = tk.Label(self, text ='Nombre: ')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0,column = 0, padx = 10, pady = 10)

        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row= 0 , column = 1, columnspan = 2)

        self.label_precio = tk.Label(self, text ='Precio: ')
        self.label_precio.config(font = ('Arial', 12, 'bold'))
        self.label_precio.grid(row = 1,column = 0, padx = 10, pady = 10)

        self.entry_precio = tk.Entry(self)
        self.entry_precio.config(width = 50, font = ('Arial', 12))
        self.entry_precio.grid(row= 1 , column = 1, columnspan = 2)

        self.label_disponible = tk.Label(self, text ='Disponible: ')
        self.label_disponible.config(font = ('Arial', 12, 'bold'))
        self.label_disponible.grid(row = 2,column = 0, padx = 10, pady = 10)

        self.entry_disponible = tk.Entry(self)
        self.entry_disponible.config(width = 50, font = ('Arial', 12))
        self.entry_disponible.grid(row= 2 , column = 1, columnspan = 2)

    #Botones
    def Botones(self):
        self.btn_nuevo = tk.Button(self,text="Nuevo", command = self.Hab_Des)
        self.btn_nuevo.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#158645', cursor = 'hand2', activebackground = '#35bd6f')
        self.btn_nuevo.grid(row = 4, column = 0, padx = 20, pady = 20)

        self.btn_guardar = tk.Button(self, text="Guardar")
        self.btn_guardar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#1658a2', cursor = 'hand2', activebackground = '#3586df')
        self.btn_guardar.grid(row = 4, column = 1, padx = 20, pady = 20)

        self.btn_cancelar = tk.Button(self, text="Cancelar")
        self.btn_cancelar.config(width = 20, font = ('Arial', 12, 'bold'),  fg = '#dad5d6', bg = '#bd152e', cursor = 'hand2', activebackground = '#e15370')
        self.btn_cancelar.grid(row = 4, column = 2, padx = 20, pady = 20)

    #Habilitar y Desabilitar Campos
    def Hab_Des(self):
        Estado = self.btn_nuevo['state']

        # Cambia el estado de los otros botones y celdas según el estado del botón Nuevo
        if Estado == tk.NORMAL:
            self.btn_guardar.config(state=tk.DISABLED)
            self.btn_cancelar.config(state=tk.DISABLED)
        else:
            self.btn_guardar.config(state=tk.NORMAL)
            self.btn_cancelar.config(state=tk.NORMAL)

if __name__=='__main__':
    main()
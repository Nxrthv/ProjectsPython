import tkinter as tk

ventana = tk.Tk()
ventana.geometry("750x450")
ventana.title("Dr. Laptop")

#Estilos
verdana = ("Verdana", 16)
Courier_New = ("Courier New", 12)
Helvica = ("Helvica", 14)


title = tk.Label(ventana, text="Guia Tecnica Dr. Laptop", font=verdana)
title.place(x=240, y=0)

#Propetario
propietario_lbl = tk.Label(ventana, text="Propietario", font=Courier_New)
propietario_lbl.place(x=60, y=40)
propietario= tk.Entry(ventana, width=50)
propietario.place(x=60, y=70)

#Telefono
telefono_lbl = tk.Label(ventana, text="Telefono", font=Courier_New)
telefono_lbl.place(x=400, y=40)
telefono = tk.Entry(ventana, width=30)
telefono.place(x=400, y=70)

#Equipo
servicio_lbl = tk.Label(ventana, text="Servicio",font=Courier_New)
servicio_lbl.place(x=60, y=95)
servicio = tk.Entry(ventana, width=40)
servicio.place(x=60, y=120)

equipo_lbl = tk.Label(ventana, text="Equipo",font=Courier_New)
equipo_lbl.place(x=340, y=95)
equipo = tk.Entry(ventana, width=40)
equipo.place(x=340, y=120)

#Reporte del Cliente
reporte_lbl = tk.Label(ventana, text="Reporte del Cliente", font=Courier_New)
reporte_lbl.place(x=60, y=150)

#Le ha caido Agua
Le_ha_caido_Agua_lbl = tk.Label(ventana, text="- Le ha Caido Agua", font=("Courier New", 10))
Le_ha_caido_Agua_lbl.place(x=60, y=180)
Le_ha_caido_Agua = tk.Checkbutton(ventana)
Le_ha_caido_Agua.place(x=350, y=180)

#No Deja ver Imagen en la Pantalla
no_deja_ver_imagen_en_la_pantalla_lbl = tk.Label(ventana, text="- No Deja ver Imagen en la Pantalla", font=("Courier New", 10))
no_deja_ver_imagen_en_la_pantalla_lbl.place(x=60, y=200)
no_Deja_ver_imagen_en_la_pantalla = tk.Checkbutton(ventana)
no_Deja_ver_imagen_en_la_pantalla.place(x=350, y=200)

#El Equipo no Enciende
el_equipo_no_enciende_lbl = tk.Label(ventana, text="- El Equipo no Enciende", font=("Courier New", 10))
el_equipo_no_enciende_lbl.place(x=60, y=220)
el_equipo_no_enciende = tk.Checkbutton(ventana)
el_equipo_no_enciende.place(x=350, y=220)

#La Bateria no Carga
la_bateria_no_carga_lbl = tk.Label(ventana, text="- La Bateria no Carga", font=("Courier New", 10))
la_bateria_no_carga_lbl.place(x=60, y=240)
la_bateria_no_carga = tk.Checkbutton(ventana)
la_bateria_no_carga.place(x=350, y=240)

#Algun Tecnico Intento Repararlo
algun_tecnico_intento_repararlo_lbl = tk.Label(ventana, text="- Algun Tecnico Intento Repararlo", font=("Courier New", 10))
algun_tecnico_intento_repararlo_lbl.place(x=60, y=260)
algun_tecnico_intento_repararlo = tk.Checkbutton(ventana)
algun_tecnico_intento_repararlo.place(x=350, y=260)

#Pantalla sin Backlight
pantala_sin_backlight_lbl = tk.Label(ventana, text="- Pantalla sin Backlight", font=("Courier New", 10))
pantala_sin_backlight_lbl.place(x=60, y=280)
pantala_sin_backlight = tk.Checkbutton(ventana)
pantala_sin_backlight.place(x=350, y=280)

#Otro Problema
otro_lbl = tk.Label(ventana, text="- Otro", font=("Courier New", 10))
otro_lbl.place(x=60, y=300)
otro = tk.Entry(ventana, width=30)
otro.place(x=120, y=300)

#Contrato de Reparacion
reporte_lbl = tk.Label(ventana, text="Pago de Servicio", font=Courier_New)
reporte_lbl.place(x=400, y=150)

#Diagnostico
diagnostico_lbl = tk.Label(ventana, text="Diagnostico", font=Courier_New)
diagnostico_lbl.place(x=400, y=180)
diagnostico25 = tk.Checkbutton(ventana, text="S/25.00")
diagnostico25.place(x=530, y=180)
diagnostico50 = tk.Checkbutton(ventana, text="S/50.00")
diagnostico50.place(x=600, y=180)

#Total
total_lbl = tk.Label(ventana, text="Total:", font=Courier_New)
total_lbl.place(x=430, y=210)
total = tk.Entry(ventana, width=15)
total.place(x=530, y=215)

#Adelanto
total_lbl = tk.Label(ventana, text="Adelanto:", font=Courier_New)
total_lbl.place(x=430, y=245)
total = tk.Entry(ventana, width=15)
total.place(x=530, y=250)

#Resta
total_lbl = tk.Label(ventana, text="Resta:", font=Courier_New)
total_lbl.place(x=430, y=280)
total = tk.Entry(ventana, width=15)
total.place(x=530, y=285)

#Reporte Tecnico
total_lbl = tk.Label(ventana, text="Reporte Tecnico", font=Courier_New)
total_lbl.place(x=60, y=340)
total = tk.Entry(ventana, width=70)
total.place(x=240, y=345)

#Boton de Enviar
btn_enviar = tk.Button(ventana, text = "Enviar", width=25)
btn_enviar.place(x=60, y=400)


ventana.mainloop()
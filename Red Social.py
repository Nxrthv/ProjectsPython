class Usuario:
    def __init__(self, username, password, birthdate, email):
        self.username = username
        self.password = password
        self.birthdate = birthdate
        self.email = email

class RedSocial:
    def __init__(self):
        self.usuarios = []

    def menu(self):
        while True:
            print("---------------------------") 
            print("Bienvenido a la Red Social!")
            print("---------------------------") 
            print("1. Registro de usuario")
            print("2. Ver perfil")
            print("3. Modificar datos")
            print("4. Salir")
            opcion = int(input("Elija una opción: "))

            if opcion == 1:
                self.registro_usuario()
            elif opcion == 2:
                self.ver_perfil()
            elif opcion == 3:
                self.modificar_datos()
            elif opcion == 4:
                print("---------------------") 
                print("Saliendo del Programa")
                print("---------------------") 
                break
            else:
                print("Opción no válida")

    def registro_usuario(self):
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        birthdate = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        email = input("Ingrese su dirección de correo electrónico: ")
        usuario = Usuario(username, password, birthdate, email)
        self.usuarios.append(usuario)
        print("-----------------") 
        print("Registro exitoso!")
        print("-----------------") 

    def ver_perfil(self):
        username = input("Ingrese su nombre de usuario: ")
        for usuario in self.usuarios:
            if usuario.username == username:
                print("------") 
                print("PERFIL")
                print("------") 
                print("Nombre de usuario: ", usuario.username)
                print("Contraseña: ", usuario.password)
                print("Fecha de nacimiento: ", usuario.birthdate)
                print("Correo electrónico: ", usuario.email)
                break
        else:
            print("Usuario no encontrado!")

    def modificar_datos(self):
        username = input("Ingrese su nombre de usuario: ")
        for usuario in self.usuarios:
            if usuario.username == username:
                opcion = int(input("Qué desea modificar?\n1. Nombre de usuario\n2. Contraseña\n3. Fecha de nacimiento\n4. Correo electrónico\nElija una opción: "))
                if opcion == 1:
                    nuevo_username = input("Ingrese su nuevo nombre de usuario: ")
                    usuario.username = nuevo_username
                elif opcion == 2:
                    nueva_password = input("Ingrese su nueva contraseña: ")
                    usuario.password = nueva_password
                elif opcion == 3:
                    nueva_birthdate = input("Ingrese su nueva fecha de nacimiento (YYYY-MM-DD): ")
                    usuario.birthdate = nueva_birthdate
                elif opcion == 4:
                    nuevo_email = input("Ingrese su nueva dirección de correo electrónico: ")
                    usuario.email = nuevo_email
                else:
                    print("Opción no válida")
                break
        else:
            print("Usuario no encontrado!")

red_social = RedSocial()
red_social.menu()
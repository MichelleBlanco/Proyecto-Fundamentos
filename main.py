import time 
import os
from pyfiglet import Figlet
from termcolor import colored
from colored import attr
from intentargenerador import generador
from validar_contraseña import verificarcontraseña
import ast

def menu():
    """Da la bienvenida al usuario y le brinda la opción de crear una cuenta o iniciar sesión con una existente
    """
    nombre_archivo = "usuarios.txt"
    
    while True:
        ListaUsuariosTotal = []
        Datos = []
    
        print("                                                                                                                ", )
        print(colored("                                                         ¡Bienvenido al Administrador                    ", "cyan", attrs=["bold", "blink"]))
        print(colored("                                                               de Contraseñas!                           ", "cyan", attrs=["bold", "blink"]))
        print("                                                                                                                 ", )
        print("                                                                                                                 ", )
        time.sleep(3)

        print(colored("Menú:", "yellow", attrs=["bold", "dark"]))
        time.sleep(1)

        print(colored("1. Iniciar Sesión",attrs=["bold", "underline"]))
        print(colored("2. Crear Cuenta",attrs=["bold", "underline"]))
        print(colored("3. Salir",attrs=["bold", "underline"]))
        opcion= input(colored("Elija una opción: ", "magenta", attrs=["bold", "dark"]))
        time.sleep(1)
        os.system("cls")  # Limpia la terminal después de elegir una opción

        if opcion == "1":
            Iniciarsecion = True
            Usuario_iniciado = " "
            while Iniciarsecion:
                with open(nombre_archivo, "r") as archivo:
                        for linea in archivo:
                            # Convertir la línea en una lista usando ast.literal_eval
                            ListaUsuariosTotal = ast.literal_eval(linea.strip())
                nombre = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
                contra = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                usuario_encontrado = False

                # Recorre la lista de usuarios para comparar nombre y contraseña
                for usuario in ListaUsuariosTotal:
                    if nombre == usuario[0]:
                        usuario_encontrado = True
                        if contra == usuario[1]:
                            print("Iniciaste sesión")
                            Usuario_iniciado = usuario[0]
                            Iniciarsecion = False
                            time.sleep(1)
                            os.system("cls")    
                        else:
                            print("El usuario o la contraseña está incorrecta")
                            time.sleep(1)
                            os.system("cls")                           
                # Si no se encontró el usuario
                if not usuario_encontrado:
                    print("Ese usuario no existe")
                    time.sleep(2)
                    os.system("cls") 
            while True:
                print(colored(f"Usuario: {Usuario_iniciado}", "yellow", attrs=["bold", "dark"]))
                time.sleep(1)
                print(colored("1. Agregar contraseña",attrs=["bold", "underline"]))
                print(colored("2. Buscar: (1)Nombre de usuario/(2)URL ",attrs=["bold", "underline"]))
                print(colored("3. Cerrar sesión",attrs=["bold", "underline"]))
                opcion= input(colored("Elija una opción: ", "magenta", attrs=["bold", "dark"]))
                time.sleep(1)
                os.system("cls")    
                if opcion == "1":
                    usuarioaplicacion = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
                    clave = input(colored("Clave maestra: ", "magenta", attrs=["bold", "dark"]))
                    direccionurl = input(colored("URL: ", "magenta", attrs=["bold", "dark"]))
                    descripción = input(colored("Descripción (opcional): ", "magenta", attrs=["bold", "dark"]))
                    fechacreacion = input(colored("Fecha de creación (opcional): ", "magenta", attrs=["bold", "dark"]))
                    time.sleep(1)
                    os.system("cls") 
                elif opcion == "2":
                    pass
                elif opcion == "3":
                    menu()

        elif opcion == "2":
            
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))

            if nombre_usuario in ListaUsuariosTotal:
                print("El usuario ya existe")
                time.sleep(2)
            else:
                Datos.append(nombre_usuario)
                OpcionContraseña= input(colored("Clave maestra: manual (1)/ generar automático (2): ", "magenta", attrs=["bold", "dark"]))
                
                time.sleep(2)
                os.system("cls")

                if OpcionContraseña == "1":
                    while True:
                        print("                                                                        ")
                        print(colored("La clave maestra debe contener:", "magenta", attrs=["bold", "dark"]))
                        print(colored("* Como mínimo 8 y como máximo 12 caracteres.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos una letra mayúscula y una minúscula.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos un número y alguno de los siguientes símbolos: #,$,@", "green", attrs=["bold", "dark"]))
                        print("                                                                        ")
                        
                        contraseña = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                        Datos.append(contraseña)
                        
                        if verificarcontraseña(contraseña):
                            contraseñaverificar = input(colored("Confirme la clave maestra: ", "yellow", attrs=["bold", "dark"]))
                            if contraseña == contraseñaverificar:
                                print(colored("Clave maestra escrita correctamente", "green", attrs=["bold"]))
                                time.sleep(3)
                                break
                            else:
                                print(colored("No coinciden, vuelva a intentarlo", "red", attrs=["bold"]))
                                time.sleep(2)
                                os.system("cls")
                        else:
                            print(colored("Clave maestra no válida, vuelva a intentarlo", "red", attrs=["bold"]))
                            time.sleep(2)
                            os.system("cls")      

                elif OpcionContraseña == "2":
                    contraseña = generador()
                    Datos.append(contraseña)
                    print(colored(f"La clave maestra es: {contraseña}", "cyan", attrs=["bold", "dark"]))
                    time.sleep(3)
                with open(nombre_usuario, "x") as archivo:
                    for elemento in Datos:
                        archivo.write(str(elemento) + "\n")

            ListaUsuariosTotal.append(Datos)        
            if os.path.exists(nombre_archivo):
                with open(nombre_archivo, "r") as archivo:
                    for linea in archivo:
                        # Convertir la línea en una lista usando ast.literal_eval
                        ListaUsuariosTotal = ast.literal_eval(linea.strip())

                    ListaUsuariosTotal.append(Datos)
                    with open(nombre_archivo, "w") as archivo:
                        archivo.write(str(ListaUsuariosTotal))

            else:
                with open(nombre_archivo, "x") as archivo:
                    ListaUsuariosTotal = str(ListaUsuariosTotal)
                    print(ListaUsuariosTotal)
                    archivo.write(str(ListaUsuariosTotal))
             

        elif opcion == "3":
            exit()

        else:
            print(colored("Opción no válida.", "red", attrs=["bold"]))
            time.sleep(2)
            os.system("cls")

menu()


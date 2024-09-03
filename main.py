import time 
import os
from pyfiglet import Figlet
from termcolor import colored
from colored import attr
from intentargenerador import generador
from validar_contraseña import verificarcontraseña

def menu():
    """Da la bienvenida al usuario y le brinda la opción de crear una cuenta o iniciar sesión con una existente
    """
    nombre_archivo = "usuarios.txt"
    lista1 = []
    while True:
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
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            contraseña = input(colored("Clave maestra: ", "magenta", attrs=["bold", "dark"]))
            # Buscar el archivo txt de un usuario
            time.sleep(3)
            os.system("cls")

        elif opcion == "2":
            lista2 = []
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))

            if nombre_usuario in lista1:
                print("El usuario ya existe")
                time.sleep(2)
            else:
                lista2.append(f"Nombre de usuario: {nombre_usuario}")
                contraseña = input(colored("Clave maestra: manual (1)/ generar automático (2): ", "magenta", attrs=["bold", "dark"]))
                time.sleep(2)
                os.system("cls")

                if contraseña == "1":
                    while True:
                        print("                                                                        ")
                        print(colored("La clave maestra debe contener:", "magenta", attrs=["bold", "dark"]))
                        print(colored("* Como mínimo 8 y como máximo 12 caracteres.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos una letra mayúscula y una minúscula.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos un número y alguno de los siguientes símbolos: #,$,@", "green", attrs=["bold", "dark"]))
                        print("                                                                        ")
                        
                        contraseña = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                        if verificarcontraseña(contraseña):
                            contraseña2 = input(colored("Confirme la clave maestra: ", "yellow", attrs=["bold", "dark"]))
                            if contraseña == contraseña2:
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

                elif contraseña == "2":
                    contraseña = generador()
                    print(colored(f"La clave maestra es: {contraseña}", "cyan", attrs=["bold", "dark"]))
                    time.sleep(3)
                
                
                lista1.append(nombre_usuario)
                with open(nombre_archivo, "w") as archivo:
                    for usuario in lista1:
                        archivo.write(f"Nombre de usuario: {usuario}\n")
                        print(lista2)
                        time.sleep(3)
                        os.system("cls")

                lista2.append(f"Clave maestra: {contraseña}")
                with open(nombre_usuario, "x") as archivo:
                    for elemento in lista2:
                        archivo.write(str(elemento) + "\n")
                
                # Añadir usuario a la lista1 y guardar en archivo principal
                with open(nombre_archivo, "w") as archivo:
                    lista1.append(lista2)
                    archivo.write(f"{lista1}\n")
                print(lista2)
                time.sleep(3)
                os.system("cls")

        elif opcion == "3":
            exit()

        else:
            print(colored("Opción no válida.", "red", attrs=["bold"]))
            time.sleep(2)
            os.system("cls")

menu()


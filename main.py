import time 
import os
from pyfiglet import Figlet
from termcolor import colored
from colored import stylize, fg, attr

def menu():
    """Da la bienvenida al usuario y le brinda la opción de crear una cuenta o iniciar sesión con una existente
    """
    while True:
        print("                                                                                                                 ", )
        print(colored("                                                         ¡Bienvenido al Administrador                    ", "cyan", attrs=["bold", "blink"]))
        print(colored("                                                               de Contraseñas!                           ", "cyan", attrs=["bold", "blink"]))
        print("                                                                                                                 ", )
        print("                                                                                                                 ", )
        time.sleep(5)

        print(colored("Menú:", "yellow", attrs=["bold", "dark"]))
        time.sleep(2)

        print(colored("1. Iniciar Sesión",attrs=["bold", "underline"]))
        print(colored("2. Crear Cuenta",attrs=["bold", "underline"]))
        print(colored("3. Salir",attrs=["bold", "underline"]))
        opcion= input(colored("Elija una opción: ", "magenta", attrs=["bold", "dark"]))
        time.sleep(1)
        os.system("cls")                        #Se encarga de limpiar la terminal después de elegir una opción

        if opcion == "1":
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            contraseña = input(colored("Contraseña: ", "magenta", attrs=["bold", "dark"]))
            time.sleep(2)
            os.system("cls")

        elif opcion == "2":
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            contraseña = input(colored("Clave maestra: ", "magenta", attrs=["bold", "dark"]))
            time.sleep(2)
            os.system("cls")

        elif opcion == "3":
            exit()

        else:
            print(colored("Opción no válida.", "red", attrs=["bold"]))
            time.sleep(2)
            os.system("cls")


menu()

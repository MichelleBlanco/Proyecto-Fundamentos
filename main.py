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
    lista1=[]
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
        os.system("cls")                        #Se encarga de limpiar la terminal después de elegir una opción

        if opcion == "1":
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            contraseña = input(colored("Clave maestra: ", "magenta", attrs=["bold", "dark"]))
            #Buscar el archivo txt de un usuario
            time.sleep(3)
            os.system("cls")

        elif opcion == "2":
            lista2=[]
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            lista2.append(f"Nombre de usuario: {nombre_usuario}")
            #guardar nombre_usuario en el txt
            contraseña = input(colored("Clave maestra: manual (1)/ generar automatico (2): ", "magenta", attrs=["bold", "dark"]))
            time.sleep(2)
            os.system("cls")

            if contraseña == "1":
                while True:
                    contraseña = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                    if verificarcontraseña(contraseña) == True:
                        contraseña2 = input(colored("Confirme la clave maestra: ", "yellow", attrs=["bold", "dark"]))
                        if contraseña == contraseña2:
                            #guardar contraseña en el .txt
                            print(colored("Clave maestra escrita correctamente", "green", attrs=["bold"]))
                            time.sleep(3)
                            break
                        else:
                            print(colored("No coinciden vuelva a intentarlo", "red", attrs=["bold"]))
                            time.sleep(2)
                    else:
                        print(colored("Clave maestra no válida, vuelva a intentarlo", "red", attrs=["bold"]))
                        time.sleep(2)
                        os.system("cls")      

            elif  contraseña == "2":
                #guardar contraseña en el .txt
                contraseña = generador()
                print(colored(f"La clave maestra es: {contraseña}", "cyan", attrs=["bold", "dark"]))
                time.sleep(3)

#INGRESA LOS DATOS DE LOS USUARIOS DE LISTA2
            lista2.append(f"Clave maestra: {contraseña}")
            time.sleep(3)

        elif opcion == "3":
            exit()

        else:
            print(colored("Opción no válida.", "red", attrs=["bold"]))
            time.sleep(2)
            os.system("cls")

#INGRESA LA LISTA2 EN LA LISTA1
        lista1.append(lista2)
        print(lista1)
        time.sleep(3)
        os.system("cls")

menu()

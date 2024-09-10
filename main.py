import time 
import os
from pyfiglet import Figlet
from termcolor import colored
from colored import attr
from intentargenerador import generador
from validar_contraseña import verificarcontraseña
import ast
from cryptography.fernet import Fernet

if not os.path.exists('clave.key'):
    clave = Fernet.generate_key()
    with open('clave.key', 'wb') as clave_archivo:
        clave_archivo.write(clave)
else:
    with open('clave.key', 'rb') as clave_archivo:
        clave = clave_archivo.read()

# Crear un objeto Fernet para cifrado/descifrado
fernet = Fernet(clave)

def encriptar(texto_plano):
    """Función para encriptar un texto plano."""
    return fernet.encrypt(texto_plano.encode()).decode()

def desencriptar(texto_cifrado):
    """Función para desencriptar un texto cifrado."""
    return fernet.decrypt(texto_cifrado.encode()).decode()

def menu():
    """Da la bienvenida al usuario y le brinda la opción de crear una cuenta o iniciar sesión con una existente
    """
    datos = []
    
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
        #time.sleep(1)
        os.system("cls")                        #Se encarga de limpiar la terminal después de elegir una opción

        if opcion == "1":
             
            nombre = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            if os.path.exists(nombre):
                with open(nombre, "r") as archivo:
                    for linea in archivo:
                        # Convertir la línea en una lista usando ast.literal_eval
                        contradocumento = ast.literal_eval(linea.strip())
                        contradocumento = desencriptar(contradocumento[1])

                contra = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                if  contra == contradocumento:                   
                    print("Iniciaste sesión")
                    time.sleep(1)
                    os.system("cls")
                    while True:
                        print(colored(f"Usuario: {nombre}", "yellow", attrs=["bold", "dark"]))
                        time.sleep(1)
                        print(colored("1. Agregar contraseña",attrs=["bold", "underline"]))
                        print(colored("2. Buscar por: Nombre de usuario",attrs=["bold", "underline"]))
                        print(colored("3. Buscar por: URL ",attrs=["bold", "underline"]))
                        print(colored("4. Cerrar sesión",attrs=["bold", "underline"]))
                        opcion_usuario= input(colored("Elija una opción: ", "magenta", attrs=["bold", "dark"]))
                        time.sleep(1)
                        os.system("cls") 

                        if opcion_usuario == "1":
                            usuarioaplicacion = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
                            if usuarioaplicacion=="":
                                print("Debe escribir un nombre de usuario")
                            else:  
                                clave = input(colored("Clave maestra: ", "magenta", attrs=["bold", "dark"]))
                                if clave=="":
                                    print("Debe escribir una clave")        
                                else: 
                                    direccionurl = input(colored("URL: ", "magenta", attrs=["bold", "dark"]))
                                    if direccionurl=="":
                                        print("Debe escribir un URL")
                                    else:
                                        descripcion = input(colored("Descripción (opcional): ", "magenta", attrs=["bold", "dark"]))
                                        fechacreacion = input(colored("Fecha de creación (opcional): ", "magenta", attrs=["bold", "dark"]))

                                        # Encriptar la clave antes de guardarla
                                        clave_encriptada = encriptar(clave)
                                        nuevosdatos = [usuarioaplicacion, clave_encriptada, direccionurl, descripcion, fechacreacion]


                                        # Abrir el archivo en modo lectura primero para obtener su contenido
                                        with open(nombre, "r") as archivo:
                                            lineas = archivo.readlines()  # Leer todas las líneas

                                        # Abrir el archivo en modo escritura para modificarlo
                                        with open(nombre, "w") as archivo:
                                            for linea in lineas:
                                                # Convertir la línea en una lista usando ast.literal_eval
                                                lista_existente = ast.literal_eval(linea.strip())
                                                lista_existente.append(nuevosdatos)  # Agregar los nuevos datos a la lista existente
                                                archivo.write(str(lista_existente) + "\n")  # Escribir la lista actualizada de vuelta al archivo

                                        time.sleep(1)
                                        os.system("cls")

                        elif opcion_usuario == "2":
                            if opcion_usuario == "2":
                                with open(nombre, "r") as archivo:
                                    lineas = archivo.readlines()  # Leer todas las líneas

                                # Procesar cada línea para mostrar los usuarios
                                print(colored("Usuarios disponibles:", "cyan", attrs=["bold", "dark"]))
                                for linea in lineas:
                                    # Convertir la línea en una lista usando ast.literal_eval
                                    lista_usuarios = ast.literal_eval(linea.strip())
                                        
                                    # Recorrer cada sublista dentro de la lista de usuarios
                                    for sublista in lista_usuarios:
                                        if isinstance(sublista, list):
                                            print("•"+sublista[0])  # Imprimir el primer elemento de cada sublista (nombre de usuario)
                                    # Solicitar input para el usuario
                                n = input(colored("Ingrese el nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
                                palabrasinfo= ["Contraseña cuenta: ","URL: ","Descripcion: ", "Fecha de creacion: "]
                                i = 0
                                    # Buscar e imprimir los datos correspondientes al usuario ingresado
                                for linea in lineas:
                                    lista_usuarios = ast.literal_eval(linea.strip())
                                    for sublista in lista_usuarios:
                                        if isinstance(sublista, list) and sublista[0] == n:
                                            print(colored("Datos del usuario:", "green", attrs=["bold"]))
                                            # Imprimir el resto de la sublista excluyendo el nombre de usuario
                                            for x in sublista[1:]:
                                                if i == 0:
                                                    if input(colored("¿Desea desencriptar la contraseña? (S/N): ","cyan", attrs=["bold"])).lower() == "s":
                                                        x = desencriptar(x)
                                                print(palabrasinfo[i] + x)
                                                i+=1 # Esto imprimirá desde el segundo elemento en adelante (contraseña, x, x, x)
                                                time.sleep(2)

                                    if input(colored("¿Desea cambiar la contraseña? (S/N): ","cyan", attrs=["bold"])).lower() == "s":
                                        clave = desencriptar(nuevosdatos[clave])
                                        nueva_contra= input(colored("Escriba una nueva contraseña: ","cyan", attrs=["bold"]))
                                        if nueva_contra=="":
                                            print("No escribió ninguna contraseña") 
                                        else:
                                            with open(nombre,"w") as archivo:
                                                nuevosdatos[clave_encriptada] = nuevosdatos[nueva_contra]
                                                archivo.write(nueva_contra)
                                                contraseña_encriptada=encriptar(nuevosdatos[nueva_contra])

                            else:
                                print("El usuario no existe")
                                time.sleep(2)
                                os.system("cls")

                        elif opcion_usuario == "3":
                            palabrasinfo= ["Nombre cuenta: ","Contraseña cuenta: ","Descripcion: ", "Fecha de creacion: "]
                            i = 0
                            with open(nombre, "r") as archivo:
                                lineas = archivo.readlines()  # Leer todas las líneas

                            # Solicitar input para la URL
                            n = input(colored("Ingrese la URL: ", "magenta", attrs=["bold", "dark"]))
                            if n == "":
                                print("No agregaste un URL")
                                
                            elif len(n)>2:
                                # Procesar cada línea
                                for linea in lineas:
                                    # Convertir la línea en una lista usando ast.literal_eval
                                    lista_usuarios = ast.literal_eval(linea.strip())
                                    
                                    # Recorrer cada sublista dentro de la lista de usuarios
                                    for sublista in lista_usuarios:
                                        if isinstance(sublista, list) and len(sublista) >= 3:
                                            # Verificar si la URL en la tercera posición coincide con n
                                            if sublista[2] == n:
                                                print(colored("Datos de la sublista (excluyendo la URL):", "green", attrs=["bold"]))
                                                # Imprimir el resto de la sublista, excluyendo la URL
                                                for x in sublista[0:2] + sublista[3:]:
                                                    if i == 1:  # Preguntar si se desea desencriptar la contraseña
                                                        if input("¿Desea desencriptar la contraseña? (S/N): ").lower() == "s":
                                                            x = desencriptar(x)
                                                    print(palabrasinfo[i] + x)
                                                    i += 1
                                    time.sleep(2)
                                    os.system("cls")
                            

                        elif opcion_usuario == "4":
                            menu()  
                else:
                    print("La contraseña está incorrecta")
                    time.sleep(2)
                    os.system("cls")                           
            else:
                print("El usuario está incorrecto")
                time.sleep(2)
                os.system("cls")   
            
                    
        elif opcion == "2":
           
            nombre_usuario = input(colored("Nombre de usuario: ", "magenta", attrs=["bold", "dark"]))
            
            if os.path.exists(nombre_usuario):
                print("El usuario ya existe")
                time.sleep(2)
                os.system("cls")

            else:
                contraseña = input(colored("Clave maestra: manual (1)/ generar automatico (2): ", "magenta", attrs=["bold", "dark"]))
                time.sleep(2)
                os.system("cls")
                if contraseña == "1":
                    datos.append(nombre_usuario)
                    while True:
                        #DAR A CONOCER A LOS USUARIOS LOS PARÁMETROS QUE SE DEBEN DE CUMPLIR PARA CREAR LA CONTRASEÑA CORRECTAMENTE
                        print("                                                                        ")
                        print(colored("La clave maestra debe contener:", "magenta", attrs=["bold", "dark"]))
                        print(colored("* Como mínimo 8 y como máximo 12 caracteres.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos una letra mayúscula y una minúscula.", "green", attrs=["bold", "dark"]))
                        print(colored("* Al menos un número y alguno de los siguientes símbolos: #,$,@", "green", attrs=["bold", "dark"]))
                        print("                                                                        ")
                        contraseña = input(colored("Clave maestra: ", "yellow", attrs=["bold", "dark"]))
                        if verificarcontraseña(contraseña) == True:
                            contraseña2 = input(colored("Confirme la clave maestra: ", "yellow", attrs=["bold", "dark"]))
                            if contraseña == contraseña2:
                                contraseña_encriptada = encriptar(contraseña)
                                datos.append(contraseña_encriptada)
                                datos = str(datos)
                                #guardar contraseña en el .txt
                                print(colored("Clave maestra escrita correctamente", "green", attrs=["bold"]))
                                time.sleep(3)
                                os.system("cls")

                                with open(nombre_usuario, "x") as archivo:
                                    archivo.write( datos + "\n")
                                break
                            else:
                                print(colored("No coinciden vuelva a intentarlo", "red", attrs=["bold"]))
                                time.sleep(2)
                                os.system("cls")
                        else:
                            print(colored("Clave maestra no válida, vuelva a intentarlo", "red", attrs=["bold"]))
                            time.sleep(2)
                            os.system("cls")      
                elif  contraseña == "2":
                    datos = []
                    datos.append(nombre_usuario)
                    contraseña = generador()
                    contraseña_encriptada = encriptar(contraseña)
                    datos.append(contraseña_encriptada)
                    datos = str(datos)
                    print(colored(f"La clave maestra es: {contraseña}", "cyan", attrs=["bold", "dark"]))
                    time.sleep(3)
                    os.system("cls")
                    with open(nombre_usuario, "x") as archivo:
                        archivo.write( datos + "\n")
        elif opcion == "3":
            exit()

        else:
            print(colored("Opción no válida.", "red", attrs=["bold"]))
            time.sleep(2)
            os.system("cls")


menu()



import random

def generador():
    """Se encarga de generar contraseñas aleatorias cada vez que el usuario lo solicite
    """
    letraminuscula= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letrasmayusculas = []
    for x in letraminuscula:
        letrasmayusculas.append(x.upper())

    numero =[0,1,2,3,4,5,6,7,8,9]
    signos = ["@","$","#"]
    n = [letraminuscula,numero,signos,letrasmayusculas]
    contraseña = ""
    contraseña += str(random.choice(numero))
    contraseña += str(random.choice(letraminuscula))
    contraseña += str(random.choice(letrasmayusculas))
    contraseña += str(random.choice(signos))
    for i in range(4):
        sele = random.choice(n)
        le = random.choice(sele)
        contraseña += str(le)
    listacontra = list(contraseña)
    random.shuffle(listacontra)
    contraseñarandom = ''.join(listacontra)
    return contraseñarandom

import re

def verificarcontraseña(contraseña):
    """Verifica que las contraseñas cumplan con los parámetros establecidos
    """
    if 8 <= len(contraseña) <= 12:
           if re.search('[a-z]', contraseña) and re.search('[A-Z]', contraseña):
                if re.search('[0-9]', contraseña):
                    if re.search('[@$#]', contraseña):
                        return True
                         
    return False

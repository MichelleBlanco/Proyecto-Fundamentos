import re


def verificarcontraseña(contraseña):
     if 8 <= len(contraseña) <= 16:
          if re.search('[a-z]', contraseña) and re.search('[A-Z]', contraseña):
               if re.search('[0-9]', contraseña):
                    if re.search('[@$#]', contraseña):
                         return True
                         
     return False

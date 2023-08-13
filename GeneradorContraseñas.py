import random
import string

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
numeros = string.digits
simbolos = "%&$=+-#"


añadir = mayusculas + minusculas + numeros + simbolos
long = random.randint(8, 16)

contraseña = "".join(random.sample(añadir, long))

print(contraseña)
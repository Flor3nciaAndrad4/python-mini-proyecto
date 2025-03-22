
# Generador de contraseñas aleatorias

# Pedir la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))
print(f"Vas a generar una contraseña de {longitud} caracteres.")
import random
import string

# Definir los caracteres posibles
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generar la contraseña
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

# Mostrar la contraseña generada
print(f"Tu contraseña aleatoria es: {contraseña}")
"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
num1 = int(numero_01) 
num2 = int(numero_02)
num3 = int(numero_03)
num4 = int(numero_04)

suma_de_numeros = num1 + num2 + num3 + num4

# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
num1 = str(numero_01)
num2 = str(numero_02)
num3 = str(numero_03)

suma_de_numeros_string = num1 + num2 + num3

# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO

numero1 = int(numero_binario, 2)
numero2 = int(numero_octal, 8)
numero3 = int(numero_hexadecimal, 16)

multiplicacion_de_numeros = numero1 * numero2 * numero3

# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO

n1 = int(numero_01)
n2 = int(numero_02, 16)
n3 = int(numero_03, 8)

resultado_resta = (((n1-n2)-n3)-numero_04)

# COMPLETAR - FIN

assert resultado_resta == -456350
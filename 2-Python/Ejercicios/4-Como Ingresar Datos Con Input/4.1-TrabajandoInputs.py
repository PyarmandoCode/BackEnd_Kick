"""
En Python, un input() es una función incorporada que sirve para leer datos que el usuario escribe por teclado mientras el programa está en ejecución.

* Lo que escribe el usuario se devuelve siempre como texto (tipo str).
* Si necesitas un número, fecha u otro tipo de dato, tienes que convertirlo manualmente.

sintaxis:
variable = input("Mensaje para el usuario:")
"""

#variable = input("Mensaje para el usuario:")
#print(f"Este es el texto ingresado {variable}")
#print(f"Tipo de datos de la variable ingresada {type(variable)}")

#conversion de tipo de datos
numero1 = input("Ingrese el valor para numero1:")
numero2 = input("Ingrese el valor para numero2:")
resultado = float(numero1) / float(numero2)
print(f"El resultado de la division es {round(resultado,2)}")
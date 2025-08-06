"""
Hacer un proyecto en Python que calcule la edad de una persona
"""
from datetime import datetime
nombre=input("Ingrese el nombre de la persona:")
nacimiento = input("Ingrese tu fecha de nacimiento (AAAA-MM-DD):")
fecha_nac=datetime.strptime(nacimiento,"%Y-%m-%d")
hoy = datetime.now()
edad = hoy.year - fecha_nac.year
print(f"{nombre} Tiene {edad} años")
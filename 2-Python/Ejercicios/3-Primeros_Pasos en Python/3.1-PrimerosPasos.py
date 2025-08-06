"""
1.-Calculadora Basica
"""
def suma(a,b):
    """Esta Funcion retorna la suma de dos valores ingresado
    Como parametros
    """
    return a + b

def restar(a,b):
    """Esta Funcion retorna la resta de dos valores ingresado
    Como parametros
    """
    return a - b

def multiplicacion(a,b):
    """Esta Funcion retorna la multiplicacion de dos valores ingresado
    Como parametros
    """
    return a * b

def division(a,b):
    """Esta Funcion retorna la division de dos valores ingresado
    Como parametros
    """
    return a / b if b !=0 else "No se puede dividir entre 0"

print("Operaciones : Suma , Resta,Multiplicacion , Division")
op = input("¿Qué Operacion desea hacer?").lower()
a= float(input("Primer Numero:"))
b= float(input("Segundo Numero:"))
if op =="suma":
    print(f"Resultado {suma(a,b)}")
elif op =="resta":
    print(f"Resultado {restar(a,b)}")    
elif op =="multiplicacion":
    print(f"Resultado {multiplicacion(a,b)}")      
elif op =="division":
    print(f"Resultado {division(a,b)}")   
else:
    print("Opcion invalida")       
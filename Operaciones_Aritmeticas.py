"""
Construir un programa que simule un menú de opciones para realizar las cuatro
operaciones aritméticas básicas (suma, resta, multiplicación y división) con dos valores
numéricos enteros. El usuario, además, debe especificar la operación con el primer
carácter de la operación que desea realizar: ‘S' o ‘s’ para la suma, ‘R’ o ‘r’ para la resta, ‘M’
o ‘m’ para la multiplicación y ‘D’ o ‘d’ para la división.
"""
print("El siguiente programa hará las operaciones aritmeticas basicas de la siguiente manera")
num1: int = int(input("Pimero digite el primer numero: "))
num2: int = int(input("digite el segundo numero: "))

print("(S) - Suma")
print("(R) - Resta")
print("(M) - Multiplicacion")
print("(D) - Division")
operacion: str = str(input("Digite la primera letra de la operacion: "))
operacion = str.upper(operacion)
if operacion == "S": print(num1+num2)
if operacion == "R": print(num1-num2)
if operacion == "M": print(num1*num2)
if operacion == "D": print(num1/num2)
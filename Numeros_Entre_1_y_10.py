"""
Escriba un programa que pida 3 notas y valide si esas notas están entre 1 y 10. Si están
entre esos parámetros se debe poner en verdadero una variable de tipo lógico y si no
ponerla en falso. Al final el programa debe decir si las 3 notas son correctas usando la
variable de tipo lógico.
"""

Nota1: int = int(input("Digite la primer nota: "))
Nota2: int = int(input("Digite la segunda nota: "))
Nota3: int = int(input("Digite la tercera nota: "))
flag = True
if (Nota1<=1) or (Nota1>=10):
    flag = False

if (Nota2<=1) or (Nota2>=10):
    flag = False

if (Nota3<=1) or (Nota3>=10):
    flag = False


if flag:
    print("Las tres notas cumplen con la condición")
else:
    print("Alguna de las tres notas no cumple con los criterios")
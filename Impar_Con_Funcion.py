"""
Realizar una función que valide si un número es impar o no. Si es impar la función debe
devolver un verdadero, si no es impar debe devolver falso. Nota: la función no debe tener
mensajes que digan si es par o no, eso debe pasar en el Algoritmo.
"""
def Impar(a):
    if a%2==0:
        return False
    else:
        return True

num: int=int(input("Digite un numero: "))
if Impar(num):
    print("El numero es Impar")
else:
    print("El numero es Par")



"""
Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación solicite
números al usuario hasta que la suma de los números introducidos supere el límite inicial
"""
Limt: int = int(input("Hasta que numero desea hacer la suma? "))
suma = 0
while True:
    num: int = int(input("Digite un numero: "))
    suma += num
    if suma > Limt:
        break
print("La suma supera el limite ingresado ",suma)
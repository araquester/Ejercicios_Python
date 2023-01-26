"""
3. Realizar un programa que pida un número y determine si ese número es par o impar.
Mostrar en pantalla un mensaje que indique si el número es par o impar. (para que un
número sea par, se debe dividir entre dos y su resto debe ser igual a 0).

"""

numero: int = int( input("Digite un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
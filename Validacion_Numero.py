"""
Escriba un programa que valide si una nota está entre 0 y 10, sino está entre 0 y 10 la nota
se pedirá de nuevo hasta que la nota sea correcta
"""
while True:
    num: float = float(input("Por favor, Digite un numero: "))
    if (num > 0) and (num < 10):
        break
    print("El numero no esta entre 1 y 10")
"""
Se pedirá una frase o palabra y se validara si la primera letra de la frase es igual a la última letra de la frase.
Se deberá de imprimir un mensaje por pantalla que diga “CORRECTO”, en caso contrario, se deberá imprimir “INCORRECTO”.
"""

palabra: str = str(input("Digite una palabra, para verificar si empieza y termina en la misma letra : "))
palabra = str.upper(palabra)
if palabra[0] == palabra[len(palabra)-1]:
    print("CORRECTO")
else:
    print("INCORRECTO")
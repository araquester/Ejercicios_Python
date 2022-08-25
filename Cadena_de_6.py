"""
4. Realizar un programa que pida introducir solo frases o palabras de 6 caracteres. Si el
usuario ingresa una frase o palabra de 6 caracteres se deberá de imprimir un mensaje por
pantalla que diga “CORRECTO”, en caso contrario, se deberá imprimir “INCORRECTO”.
Nota: investigar la función Longitud()
"""
cadena: str = str(input("Digite una frase: "))
if len(cadena) == 6:
    print("La palabra tiene 6 caracteres es: CORRECTA")
else:
    print("La palabra tiene: ",len(cadena)," caracteres es: INCORRECTA")

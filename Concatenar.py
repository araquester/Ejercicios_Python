"""
Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4
caracteres de largo, el programa le concatenara un signo de exclamación al final, y si no
es de 4 caracteres el programa le concatenara un signo de interrogación al final. El
programa mostrará después la frase final. Nota: investigar la función Longitud() y
Concatenar()
"""

# Recibe la palabra
palabra: str = str(input("Digite una palabra: "))

#verifico si la longitud es de 4 caracteres e imprimo
if len(palabra) == 4:
    #primer manera de concatenar
    print(palabra + "!")
    #segunda manera de concatenar
    print("%s""!" %(palabra))
    #tercera manera de concatenar
    print(f"{palabra}""!")
else:
    #primer manera de concatenar
    print(palabra + "?")
    #segunda manera de concatenar
    print("%s""?" %(palabra))
    #tercera manera de concatenar
    print(f"{palabra}""?")



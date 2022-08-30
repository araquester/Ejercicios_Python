"""
Realizar un programa que pida una frase y el programa deberá mostrar la frase con un
espacio entre cada letra. La frase se mostrará así: H o l a
"""
palabra: str = str(input("Digite una palabra: "))
rango = len(palabra)
for i in range(0,rango):
    print(f"{palabra[i]}", end=" ")


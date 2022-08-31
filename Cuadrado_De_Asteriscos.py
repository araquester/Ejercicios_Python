"""
Realizar un programa que lea un número entero (tamaño del lado) y a partir de él cree un
cuadrado de asteriscos de ese tamaño. Los asteriscos sólo se verán en el borde del
cuadrado, no en el interior
"""
lado: int = int(input("De que tamaño es el lado del cuadrado: "))
for i in range(1,lado+1):
    for j in range(1,lado+1):
        if i==1 and (j!= lado):
            print("*",end=" ")
            continue
        elif i==1 and j==lado:
            print("*")
            continue
        elif i==lado and j!=lado:
            print("*",end=" ")
            continue
        elif i==lado and j==lado:
            print("*")
            continue
        elif (lado>i>1) and (j==1):
            print("*",end=" ")
        elif (lado>i>1) and (lado>j>1):
            print(" ",end=" ")
        elif (lado>i>1) and (j==lado):
            print("*")
            continue

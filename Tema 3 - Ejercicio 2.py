"""
Escribe un programa en la consola de python que
pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable
, e imprima por pantalla la frase Tu índice de masa corporal es donde
es el índice de masa corporal calculado redondeado con dos decimales.
"""

#Asignar a una variable una entrada
peso = input("¿Cual es tu peso en Kg? ")
estatura = input("¿Cual es tu estatura? ")
IMC = round(float (peso)/float (estatura)**2,2) ##Calculamos el indice de masa
print ("Tu indice de masa corporal es " + str(IMC))

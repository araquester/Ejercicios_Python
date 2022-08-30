"""
Escriba un programa para obtener el grado de eficiencia de un operario de una fábrica de
tornillos, de acuerdo a las siguientes dos condiciones que se le imponen para un período
de prueba:
• Producir menos de 200 tornillos defectuosos.
• Producir más de 10000 tornillos sin defectos.
• El grado de eficiencia se determina de la siguiente manera:
• Si no cumple ninguna de las condiciones, grado 5.
• Si sólo cumple la primera condición, grado 6.
• Si sólo cumple la segunda condición, grado 7.
• Si cumple las dos condiciones, grado 8
"""
Total: int = int(input("Cual fue el numero total de tornillos manufacturados sin defectos : "))
defecto: int = int(input("Y el numero de tornillos defectuosos : "))

efic = 0
if defecto > 200 and Total < 10000:
    efic = 5
else:
    if defecto < 200 and Total < 10000:
        efic = 6
    else:
        if defecto > 200 and Total > 10000:
            efic = 7
        else:
            efic = 8
print("El grado de eficiencia del trabajador es: Grado ",efic)



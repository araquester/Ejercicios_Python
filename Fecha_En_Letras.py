"""
Leer tres números que denoten una fecha (día, mes, año) y comprobar que sea una fecha
válida. Si la fecha no es válida escribir un mensaje de error por pantalla. Si la fecha es
válida se debe imprimir la fecha cambiando el número que representa el mes por su
nombre. Por ejemplo: si se introduce 1 2 2006, se deberá imprimir “1 de febrero de 2006”.
"""
dia = 1
mes = 1
anio = 1
while True:
    dia: int = int(input("Digite el dia : "))
    if (dia>=1) and (dia<32):
        break
    else: print("el dia no es valido")
while True:
    mes: int = int(input("Digite el mes : "))
    if (mes>=1) and (mes<=12):
        break
    else: print("el mes no es valido")
anio: int = int(input("Digite el año : "))
match mes:
    case 1: mes = "Enero"
    case 2: mes = "Febrero"
    case 3: mes = "Marzo"
    case 4: mes = "Abril"
    case 5: mes = "Mayo"
    case 6: mes = "Junio"
    case 7: mes = "Julio"
    case 8: mes = "Agosto"
    case 9: mes = "Septiembre"
    case 10: mes = "Octubre"
    case 11: mes = "Noviembre"
    case 12: mes = "Diciembre"
print("%i " %dia, "%s " %mes,"%i " %anio)



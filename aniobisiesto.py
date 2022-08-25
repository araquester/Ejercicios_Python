anio : int =int(input("Digite un año para saber si es bisiesto:  "))

def bisiesto(numero):
    if numero != 1900:
        if numero % 4 == 0:
            if (numero % 100 != 0) or (numero % 400 == 0):
                return True
            else:
                return False
    else:
        return True


if bisiesto(anio):
    print("el año ",anio,"es bisiesto")
else:
    print("el año ",anio,"no es bisiesto")
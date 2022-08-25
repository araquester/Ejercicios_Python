"""Escribe una función que pueda decirte si un número (número entero) es primo o no."""

def primo(a):
    if a>1:
        for i in range(2,a):
            if (a%i == 0):
                print("El numero no es primo es divisible por: ",i)
                break
            else:
                print("Felicitaciones el numero es primo")
                break
    else:
        print("Lo sentimos los numeros primos son mayores a 1")

numero: int = int(input("Digite un numero? "))
primo(numero)

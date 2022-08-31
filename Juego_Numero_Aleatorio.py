"""
 Programar un juego donde la computadora elige un número al azar entre 1 y 10, y a
continuación el jugador tiene que adivinarlo. La estructura del programa es la siguiente:
1o) El programa elige al azar un número n entre 1 y 20.
2o) El usuario ingresa un número x.
3o) Si x no es el número exacto, el programa indica si n es más grande o más pequeño que
el número ingresado.
4o) Repetimos desde 2) hasta que x sea igual a n.
El programa tiene que imprimir los mensajes adecuados para informarle al usuario qué
hacer y qué pasó hasta que adivine el número.
"""
import random
n = random.randint(1,20)
while True:
    x: int = int(input("Digite un numero entre 1 y 20: "))
    if x < n:
        print("El numero deseado es mayor")
        continue
    if x > n:
        print("El numero deseado es menor")
        continue
    if x == n:
        print(f"{x} era el numero deseado")
        break

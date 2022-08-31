"""
Realizar una función que calcule la suma de dos números. En el algoritmo principal le
pediremos al usuario los dos números para pasárselos a la función. Después la función
calculará la suma y lo devolverá para imprimirlo en el algoritmo.
"""
def suma(a,b):
    return a + b
# Esta es la forma tradicional
Num1: int = int(input("Digite el primer numero: "))
Num2: int = int(input("Digite el segundo numero: "))
print(f"{Num1} + {Num2} = {suma(Num1,Num2)}")

# Con función anonima es de esta manera

Suma2 = lambda Num1,Num2 :Num1 + Num2
print(f"{Num1} + {Num2} = {Suma2(Num1,Num2)}")
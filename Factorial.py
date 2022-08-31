"""
 La función factorial se aplica a números enteros positivos. El factorial de un número entero
positivo (!n) es igual al producto de los enteros positivos desde 1 hasta n:
n! = 1 * 2 * 3 * 4 * 5 * (n-1) * n
Escriba un programa que calcule las factoriales de todos los números enteros desde el 1
hasta el 10. El programa deberá mostrar la siguiente salida:
!1 = 1
!2 = 1*2 = 2
...
!5 = 1*2*3*4*5 = 120
"""
facto = 1
print(f"!1 = {facto}")
for i in range(2,11):
    facto*=i
    print(f"!{i} = {facto}")
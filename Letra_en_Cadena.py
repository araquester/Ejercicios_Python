"""
Realizar un programa que pida al usuario una frase y una letra a buscar en esa frase. La
función debe devolver la cantidad de veces que encontró la letra.
"""
def ValidaLetra(Cadena,Char):
    Final = len(Cadena)
    Cont = 0
    for i in range(0,Final):
        if Cadena[i] == Char:
            Cont+=1
    return Cont


Frase: str=str(input("Digite una frase: "))
Letra: str=str(input("Digite la letra a buscar: "))
print(f"La Letra {Letra} se enccuentra {ValidaLetra(Frase,Letra)} veces en la Frase")
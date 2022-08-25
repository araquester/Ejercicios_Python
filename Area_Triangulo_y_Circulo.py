import math

def AreaTriangulo(Base, Altura):
    return ((Base*Altura)/2)

def AreaCirculo(Radio):
    return math.pi*Radio**2

print(f"Area del Triangulo: ", AreaTriangulo(2,2))
print(f"Area del Circulo: ", AreaCirculo(4))
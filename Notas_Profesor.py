"""
Un docente de Programación tiene un listado de 3 notas registradas por cada uno de sus
N estudiantes. La nota final se compone de un trabajo práctico Integrador (35%), una
Exposición (25%) y un Parcial (40%). El docente requiere los siguientes informes claves de
sus estudiantes:
§ Nota promedio final de los estudiantes que reprobaron el curso. Un estudiante
reprueba el curso si tiene una nota final inferior a 6.5
§ Porcentaje de alumnos que tienen una nota de integrador mayor a 7.5.
§ La mayor nota obtenida en las exposiciones.
§ Total de estudiantes que obtuvieron en el Parcial entre 4.0 y 7.5.
El programa pedirá la cantidad de alumnos que tiene el docente y en cada alumno pedirá
las 3 notas y calculará todos informes claves que requiere el docente.
"""
contador = 1
Decision = "S"
NotaPromFinal = 0
ContaReprob = 0
ContNotaIntegraMay = 0
MayorExposici = 0
ContadorParcial = 0
while True:
    TrabPracInteg: float = float(input("Digite la nota del trabajo practico integrador: "))
    if TrabPracInteg > 7.5:
        ContNotaIntegraMay+=1
    Exposi: float = float(input("Digite la nota de la Exposicion: "))
    if Exposi > MayorExposici:
        MayorExposici = Exposi
    Parcial: float = float(input("Digite la nota del parcial: "))
    if (4.0<Parcial<7.5):
        ContadorParcial+=1
    NotaFinal = (TrabPracInteg*0.35)+(Exposi*0.25)+(Parcial*0.4)
    print(f"La nota fina del estudiante es: {NotaFinal}")
    if NotaFinal < 6.5:
        NotaPromFinal+=NotaFinal
        ContaReprob+=1
    while True:
        Decision: str = str(input("Desea digitar las notas de otro estudiante: (S) Si o (N) No: "))
        Decision = str.upper(Decision)
        print(f"{Decision}")
        if (Decision == "S") or (Decision == "N"):
            break
    if (Decision == "N"):
        break
    else:
        contador+=1
print(f"La nota promedio final de los estudiantes que reprobaron el curso es: ",NotaPromFinal/ContaReprob)
print(f"Porcentaje de alumnos que tienen una nota de integrador mayor a 7.5: ",(ContNotaIntegraMay/contador)*100)
print(f"La mayor nota obtenida en las exposiciones es : ",MayorExposici)
print(f"El Total de estudiantes que obtuvieron en el Parcial entre 4.0 y 7.5. es: ",ContadorParcial)
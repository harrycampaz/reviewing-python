#If sencillo
print("Inicia la Super App")

nota_alumno = input("Introduce la nota: ")

def check(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Reprobado"
    return valoracion

print(check(int(nota_alumno)))

# if else

print("verificacion if else")

edad = int(input("Introduce la edad: "))

if edad < 18 and edad > 0:
    print("no es mayor de edad")
elif edad > 100 or edad < 0:
    print("Edad incorrecta")
else:
    print("Es mayor de edad")


edad = 7

if 0< edad < 100:
    print("edad correcta")
else:
    print("edad incorrecta")

salarioP = int(input("Presidente: "))
print("Salario: " + str(salarioP))

salarioD = int(input("Director: "))
print("Salario: " + str(salarioD))

salarioJ = int(input("Jefe: "))
print("Salario: " + str(salarioJ))

if salarioJ < salarioD < salarioP:
    print("Todo bien con los sueldos")
else:
    print("hay algun problema")

#And OR I

print("programa de becas")

asignatura =  input("Ingresar asignatura: ").lower()

if asignatura in ("fisica", "informatica", "matematicas"):
    print("Si esta en la asignatura: " + asignatura)
else:  
    print("No puedes ver esta asignatura")

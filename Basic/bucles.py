#FOR

for i in [1,2,3]:
    print(i)

#End
for i in [1,2,3]:
    print(i, end=" ")


for i in "Caracteres":
    print(i, end=" ")


email = False;
for i in "miemail@data.com":
    if i =="@":
        email = True

if email:
    print("Email Correcto")
else: 
    print("Email incorrecto")
# Contador
count =0
email = False;
for i in "miemail@data.com":
    if i =="@" or i ==".":
        count = count + 1

if count == 2:
    print("Email Correcto")
else: 
    print("Email incorrecto")

#Range

for i in range(5):
    print("Hara" + str(i))


#Range notacion espacial

for i in range(5):
    print(f"Hara {i}")

#Range inversio

for i in range(3, 5):
     print(f"Hara {i}")

for i in range(3, 20, 2):
     print(f"Hara {i}")

#For len and range
count = 0
email = "miemail@data.com"
for i in range(len(email)):
    if email[i] =="@" or email[i] ==".":
        count = count + 1

if count == 2:
    print("Email Correcto")
else: 
    print("Email incorrecto")

#------------WHILE--------------

i = 1

while i <= 10:
    print(f"Num: {i}")
    i = i + 1

import math
num = int(input("Introducir un numero: "))

intentos = 0

while num < 0:
    print("Numero negativo, no se puede halla raiz cuadrada")

    if intentos == 2:
        print("Ya no tienes mas intentos")
        break;
    num = int(input("Introducir un numero: "))
    if num < 0:
        intentos = intentos + 1


if intentos < 2:
    solucion = math.sqrt(num)
    print(f"Solucion al problemas es: {solucion}")

print("Programa finalizado")

# Continue pass y else 

for i in "My Application":
    if i == "i":
        continue
    print(f"Viendo la letra {i}")


name = "Texto de informatica"
counter = 0
for i in name:
    if i == " ":
        continue
    counter += 1
print(counter)

email = "correo@data.com"

for i in email:
    if i == "@":
        arroba = True
        break;
else: 
    arroba = False

print(arroba)

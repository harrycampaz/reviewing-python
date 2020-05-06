
# Functions
def mensaje():
    print('My Functions')
# mensaje()

# Function con parametros
def suma(num1, num2):
    print(num1 + num2)

# suma(2,1)


# Function con parametros and return
def suma(num1, num2, num3):
    return num3 * num2 + num1

# print(suma(2,1,2))

# Listas o Arrays

# lista = ["Primero", "Segundo", "Tercero", "Cuarto", "Quinto"]
# lista.append("Sexto")
# lista.insert(0, "Cero")
# lista.extend(["Septimo", "Octavo"])
# #Todos los datos con [:]
# # print(lista[:])
# # #Acceso invertido
# # print(lista[-2])

# # print(lista[1:3])

# print(lista[:])
# print(lista.index("Sexto"))

# print("Cero" in lista)

# listaMixta = ["Cero",1, 2, "Tres"]

# # print(listaMixta[:])

# print(listaMixta[1])
# print(2 in listaMixta)

# listaMixta.remove(2)

# print(listaMixta[:])

# listaMixta.pop()

# print(listaMixta[:])

# listaMixta2 = ["Primero", "Decimo"]

# listaMixta3 = listaMixta + listaMixta2

# print(listaMixta3[:])

# # Tuplas

# miTupla = ("Primero", 2, "Tercero", 4 , 5, "sexto", 2)
# empaquetadoTupla = "Diez", 22, "11"

# diez, ventidos, once = empaquetadoTupla


# miLista = list(miTupla)

# print(miTupla[:])

# print(miLista[:])

# segundaTupla = tuple(miLista)

# print(segundaTupla)

# print(2 in miTupla)

# print(miTupla.count(2))

# print(len(miTupla))

# #Tupla Unitaria

# tuUnitaria = ("Sola",)
# print(len(tuUnitaria))

# print(empaquetadoTupla[:])
# print(diez)

# # Diccionarios

# miDiccionario= {"Colombia": "Bogota", "UK": "Londres", "Espana": "Madrid" }
# miDiccionario["Uruguay"] = "La Paz"
# print(miDiccionario["Colombia"])

# print(miDiccionario)

# miDiccionario["Uruguay"] = "Montevideo"

# print(miDiccionario)

# del miDiccionario["UK"]

# print(miDiccionario)


# miDiccionario= {"Colombia": "Bogota", 42: "Numero de vida", 3: "CP3" }

# print(miDiccionario)


# tupla = ["Francia", "Alemania", "vanezuela"]

# miDiccionarioConTuple = {tupla[0]: "Bogota", tupla[1]: "Berlin", tupla[2]: "Caracas"}

# print(miDiccionarioConTuple)


# miDiccionario= {23: "James", "Name": "Lebron", "finales": [2010, 2011, 2012, 2013, 2014]}

# print(miDiccionario["finales"])


# print(miDiccionario.keys())

# print(miDiccionario.values())

# print(len(miDiccionario))

# data = 'Dotos'

# no = data.lower()

# print(no)

# lista = range(3)


# for i in range(3):
#     print(i)

# def factorial(n):

#     print(n)
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# n = int(input('Escribe un numero'))

# print(factorial(n))
5 / 'Platzi' 


def form(x):
	respuesta = 0
	for i in range (2000):
	    respuesta += 1

return respuesta



form(2)
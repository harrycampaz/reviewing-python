#generadores

def pairGenerator(limit):
    num = 1
    

    while num < limit:
       yield num * 2
       num += 1


misPares = pairGenerator(30)


# for i in misPares:
#     print(i)

print(next(misPares))
print(next(misPares))
print(next(misPares))
print(next(misPares))



# Yield from

def ciudadesGenerator(*ciudades):
    for i in ciudades:
        for j in i:
            yield j

def ciudadesGenerator(*ciudades):
    for i in ciudades:
        yield from i


ciudadesAll = ciudadesGenerator("Berlin", "Cali", "Bogota", "Atlante")

print(next(ciudadesAll))

import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo :
            match = True
            break
    return match


def main():
    tamano = int(input("Tamano de la lista ?"))

    objetivo = int(input("Que numero quieres encontrar"))

    lista = [random.randint(0, 100) for i in range(tamano) ]
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)

    print(f'El elemento {objetivo} {"esta"  if encontrado else "No esta"} en la lista')


if __name__ == '__main__':
    main()
    





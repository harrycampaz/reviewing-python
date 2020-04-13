import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
      for j in range(0, (n - i) - 1):
          if lista[j] > lista[j + 1]:
              lista[j], lista[j + 1] = lista [j + 1], lista[j]
    return lista


def main():
    tamano = int(input("Tamano de la lista ?"))

    # objetivo = int(input("Que numero quieres encontrar"))

    lista = [random.randint(0, 100) for i in range(tamano) ]

    print(lista)

    ordenado = ordenamiento_burbuja(lista)


    print(ordenado)




if __name__ == '__main__':
    main()
    





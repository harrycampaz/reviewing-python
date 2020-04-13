import random

def ordenamiento_por_insercion(lista):
    
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista


def main():
    tamano = int(input("Tamano de la lista ?"))

    # objetivo = int(input("Que numero quieres encontrar"))

    lista = [random.randint(0, 100) for i in range(tamano) ]

    print(lista)

    ordenado = ordenamiento_por_insercion(lista)


    print(ordenado)




if __name__ == '__main__':
    main()
    





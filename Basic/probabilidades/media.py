import random
import math

def media (X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu) ** 2

    return acumulador / len(X)
def desviacio_estandar(X):
    return math.sqrt(varianza(X))

def main():
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)

    Var = varianza(X)
    sigma = desviacio_estandar(X)

    

    print(f'Arreglo: {X}')
    print(f'Media: {mu}')
    print(f'varianza: {Var}')
    print(f'desviacion estandar: {sigma}')

if __name__ == '__main__':
     main()


    
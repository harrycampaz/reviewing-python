def divide(num1, num2):
    try:
        print("El resultado es " + str(num1/num2))
    except ZeroDivisionError:
        print("No se puede dividi en 0")

divide(4,2)


def divide(num1, num2):
    try:
        print("El resultado es " + str(num1/num2))
    except ZeroDivisionError:
        print("No se puede dividi en 0")
    except TypeError:
         print("Tipo de Variable incorrecta")
    except:
        print("Ha ocurrido un error")

    finally:
        print("calculo terminado")

divide(4,1)


def checkEdad(edad):

    if edad < 0:
        raise ValueError("No se permiten fechas negativas")

    if edad < 20:
        return "Joven"
    elif edad < 40:
        return "Maduro"
    elif edad < 90:
        return "Viejo"

try:
    print(checkEdad(30))
except ValueError as msg:  
    print(msg)

import math

""" import datetime

def EvaluarEdad():
    fecha_nacimiento = int(input("Introduce tu fecha de nacimiento: "))
    get_date_now = datetime.datetime.now()
    get_year_now = get_date_now.year
    edad = get_year_now - fecha_nacimiento

    if fecha_nacimiento < 0:
        raise ValueError("La fecha de nacimiento no puede ser negativa")
    elif get_year_now - fecha_nacimiento >99:
        raise Warning("La edad no puede ser mayor a 99")
    else:
        if  edad > 0 and edad < 18:
            print("Eres menor de edad")
            format = "Tu edad Actual es: {} Años"
            return format.format(edad)
        elif edad >= 18 and edad <= 30:
            print("Eres mayor de edad")
            format = "Tu edad Actual es: {} Años"
            return format.format(edad)
        elif edad > 30 and edad < 40:
            print("Eres un adulto joven")
            format = "Tu edad Actual es: {} Años"
            return format.format(edad)
        elif edad > 40 and edad < 60:
            print("Ya eres un adulto mayor")
            format = "Tu edad Actual es: {} Años"
            return format.format(edad)
        elif edad > 60:
            print("Eres una persona vieja")
            format = "Tu edad Actual es: {} Años"
            return format.format(edad)

        


print(EvaluarEdad()) """


def cal_raiz_cuadrada(numero):
    try:
        numero = int(numero)
        if numero < 0:
            raise ValueError("El numero no puede ser negativo")
        else:
            return math.sqrt(numero)
    except ValueError as error:
        print(error)


print(cal_raiz_cuadrada(45))
print(cal_raiz_cuadrada(345))
print(cal_raiz_cuadrada(-424))
print(cal_raiz_cuadrada(144))

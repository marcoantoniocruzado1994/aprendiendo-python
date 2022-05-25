#GENERADORES
#Generadores son funciones que devuelven un objeto iterable(osea se puede recorrer)

#yield es una palabra reservada que permite generar un objeto iterable

""" def generarPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1

devuelve_parses = generarPares(10)

print(next(devuelve_parses)) #entre llamada y lamada la funcion se detiene y entra en un estado de espera
print("es algo asi como una lista de pares")
print(next(devuelve_parses))
print("es algo asi como una lista de pares")
print(next(devuelve_parses))

#vamos a hacer un progrma

#siguiente_valor  = input("Presiona enter para continuar....")

from pynput.keyboard import Key, Listener 

limite = int(input("Introduce un limite: "))
input("Presiona enter para continuar....")

def generar_numeros_impares(limite):
    #validar que la entrada sea numeros
    if not isinstance(limite, int):
        print("El limite debe ser un numero")
        return
    else:
        num = 1
        while num < limite:
            yield num
            num += 2
    
devuelve_impares = generar_numeros_impares(limite)

#devolver lista genrada mientras la tecla pulsada sea enter

def show(key):
    if key == Key.enter:
        print(next(devuelve_impares))
        input("Presiona enter para continuar....")
    else:
        print("Tecla no valida se acabo el programa")
        return False

with Listener(on_press=show) as listener:
    listener.join()
    """

#GENERADORES DOS

def devuelve_ciudades(*ciudades): # * significa que se puede recibir un numero indeterminado de argumentos y se guardan en una tupla
    for ciudad in ciudades:
        #for subLetra in ciudad:
            yield from ciudad

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


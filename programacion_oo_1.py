class Coche():
    def __init__(self):
        """ Constructor """
        """ Con los dos guión bajo se puede acceder a los atributos privados  o encapsulados """
        self.__ruedas = 4
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__enmarcha = False

    """ Self es una referencia a la clase """
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        format = "El coche tiene {} ruedas \n" \
                    "El largo del chasis es {} cm \n" \
                    "El ancho del chasis es {} cm"
        return format.format(self.__ruedas,self.__largo_chasis,self.__ancho_chasis)


""" Instanciar una clase """
coche_langorgini = Coche()

print(coche_langorgini.arrancar(True))
print(coche_langorgini.estado())

print("==========================================")

""" Instanciar una clase """
coche_ferrari = Coche()

print(coche_ferrari.arrancar(False))
print(coche_ferrari.estado())

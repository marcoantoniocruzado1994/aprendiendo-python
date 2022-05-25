#vamos a crear una clase padre y que heredaran a sus hijos 

class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        format = "Marca: {} \nModelo: {} \nEn marcha: {} \nAcelerando: {} \nFrenando: {}"
        print(format.format(self.marca,self.modelo,self.enmarcha,self.acelera,self.frena))

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar #true o false
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        super().estado()
        print(self.hcaballito)

class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


motocicleta = Moto("Honda","CBR")
motocicleta.caballito()
motocicleta.estado()
print("==========================================")
furgon = Furgoneta("Renault","Kangoo")
furgon.arrancar()
furgon.estado()
print(furgon.carga(True))
print("==========================================")

class BicicletaElectrica(VElectricos,Vehiculos): #aca es importante el orden de las clases 
    pass


mi_bici = BicicletaElectrica()
print(mi_bici.estado())
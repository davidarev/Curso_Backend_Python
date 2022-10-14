from random import randint

class CuentaBancaria():
    #Propiedades
    __IBAN = ""
    titular = ""
    __saldo = 0

    #Constructor
    def __init__(self, Titular):
        self.titular = Titular
        self.__generar_IBAN() #Cuando creamos un objeto, el constructor llama a la funcion automaticamente

    #Getters y Setters
    #Manera simple
        def get_IBAN(self):
            return self.__IBAN
        def set_IBAN(self, Iban): #El usuario tiene permiso de escritura, si "cuenta.set_IBAN(0)", el IBAN cambia
            self.__IBAN = Iban
        def get_saldo(self):
            return self.__saldo
        def set_saldo(self, Saldo): #El usuario tiene permiso de escritura, si "cuenta.set_saldo(0)", el saldo cambia
            self.__saldo = Saldo
    #Manera Pro
        @property
        def IBAN(self):
            return self.__IBAN
        @IBAN.setter
        def IBAN(self, Iban):  #El usuario tiene permiso de escritura, si "cuenta.set_IBAN(0)", el IBAN cambia
            self.__IBAN = Iban
        @property
        def saldo(self):
            return self.__saldo
        @saldo.setter
        def saldo(self, Saldo):  #El usuario tiene permiso de escritura, si "cuenta.set_saldo(0)", el saldo cambia
            self.__saldo = Saldo

    #Metodos
    def __generar_IBAN(self):
        print("IBAN generado")
        self.__IBAN = randint(0, 99999999)
    def añadir_dinero(self, dinero):
        if(dinero > 0):
            print("Se ha añadido dinero correctamente")
            self.__saldo += dinero
    def sacar_dinero(self, dinero):
        if(dinero > 0):
            print("Se ha retirado dinero correctamente")
            self.__saldo -= dinero


cuenta = CuentaBancaria("David Arevalo Ortega")
print(cuenta.IBAN)              #Manera Pro usando propiedades
#print(cuenta.get_IBAN())       #Manera Simple
cuenta.añadir_dinero(4500)
print(cuenta.saldo)             #Manera Pro usando propiedades
#print(cuenta.get_saldo())      #Manera Simple
cuenta.sacar_dinero(500)
print(cuenta.saldo)
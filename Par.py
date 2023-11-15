class Par():
    def __init__(self):
        self.numero = int(input("Ingresa un numero: "))
        
    def dividiendo (self):
        if  self.numero % 2 == 0:
            print("Su numero PAR")
        else:
            print("Su numero es IMPAR")
            
    def imprimir(self):
        print(f"El numero ingresado fue: {self.numero}")

llamando_numero = Par()
llamando_numero.dividiendo()
llamando_numero.imprimir()

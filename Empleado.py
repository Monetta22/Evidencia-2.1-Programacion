class Empleado():
    def __init__(self):
        self.nombre = input("Ingresa su nombre:")
        self.sueldo = float(input("Ingresa su sueldo: "))
        
    def imprimir(self):
        print(f"Tu nombre es: {self.nombre}")
        print(f"Tu sueldo es: {self.sueldo}")
        
    def paga_impuestos(self):
        if self.sueldo >3000:
            print("Usted paga impuestos")
        else:
            print("Usted no paga impuestos")
        
empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
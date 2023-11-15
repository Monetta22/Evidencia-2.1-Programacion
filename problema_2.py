class Alumno:
    
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"El nombre del alumno es: {self.nombre}")
        print(f"La nota del alumno es: {self.nota}")
        
    def mostrar_estado(self):
        if self.nota >= 4:
            print("Estado REGULAR")
        else:
            print("Estado LIBRE")   
            
print("============Alumno numero 1============")        

alumno1 = Alumno()
alumno1.inicializar("Pablo", 10)
alumno1.imprimir()
alumno1.mostrar_estado()

print("================================================================")

print("============Alimno numero 1============")        

alumno2 = Alumno()
alumno2.inicializar("Carlos", 2)
alumno2.imprimir()
alumno1.mostrar_estado() 
        
        
        
        
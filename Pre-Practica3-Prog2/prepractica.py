from traceback import print_tb


class vehiculo:
    def __init__(self,marca: str,ruedas: int,color: str,enMarcha: bool):
        self.marca: str = marca
        self.ruedas: int = ruedas
        self.color: str = color
        self.enMarcha: bool = False
        
    def arracar(self):
        self.enMarcha = True
    
    def tipoVehiculo(self):
        if self.ruedas == 4:
            return print("Automóvil")
        elif self.ruedas == 2:
            return print("Motocicleta")
        else:
            return print("Camión")
        
    def mostrar(self):
        return print("Marca", self.marca,"\nColor",self.color,"\nCantidad de ruedas",self.ruedas,"\nEn marcha",self.enMarcha)
    
auto1 = vehiculo("Ford",6,"rojo",False)

auto1.arracar()

auto1.mostrar()

auto1.tipoVehiculo()
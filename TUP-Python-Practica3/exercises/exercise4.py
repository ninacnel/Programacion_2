"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List


"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""

@dataclass
class Carrera:
    materias:str
    
    def __len__(self): 
        return len(self.materias)
    
@dataclass
class Materia:
    nombre:str

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    materia = Materia()
    assert False, "No se puede instanciar sin nombre"
except TypeError:
    assert True

try:
    materia = Carrera()
    assert False, "No se puede instanciar sin materias"
except TypeError:
    assert True

# Test básico
matematica = Materia("Matemática")
assert matematica.nombre == "Matemática"

estadistica = Materia(nombre="Estadística")
assert estadistica.nombre == "Estadística"

filosofia = Materia("Filosofia")
assert filosofia.nombre == "Filosofia"

ciclo_basico = Carrera([matematica, estadistica, filosofia])
assert (
    str(ciclo_basico)
    == "Carrera(materias=[Materia(nombre='Matemática'), Materia(nombre='Estadística'), Materia(nombre='Filosofia')])"  # noqa: 501
)

assert len(ciclo_basico) == 3
# NO MODIFICAR - FIN
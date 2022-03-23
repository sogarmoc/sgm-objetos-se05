# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 15/03/22

# reto 1 poo

class Alumno():
    # Atributos de clase

    nombre: str
    apellidos: str
    __dni: str
    edad: int
    nota= []
    asignaturas = []


    # Constructor de clase que queramos pasar si o si para la clase
    def __init__(self, newNom, newApe,newDNI,newEdad):
        self.nombre = newNom
        self.apellidos = newApe
        self.__dni = newDNI
        self.edad = newEdad
        self.nota = []
        self.asignaturas = []

    # Comportamiento - metodos de clase

    def saludar(self):
        print(f'Bienvenido {self.nombre}, {self.apellidos}')

    def nota(self,newNota):
        if 0 <= newNota <= 10:
            self.nota.append(newNota)
        else:
            print('Introduce nota valida:')

    def anyos(self):
        self.edad += 1
        print(f'Tu edad es {self.edad}')


# Fingir que es privado (encapsular)

    @property  # El getter
    def dni(self):
         return self.__dni
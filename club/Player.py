# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 15/03/22

class Player():
    # Atributos de clase
    nombre: str
    edad: int
    rol: str

    # Constructor de clase
    def __init__(self, newNom, newEdad, newRol):
        self.nombre = newNom
        self.edad = newEdad
        self.rol = newRol

    # Metodos de clase -  comportamiento

    def saluda(self):
        print(f'Hola {self.nombre}')

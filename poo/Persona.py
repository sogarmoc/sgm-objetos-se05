# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 15/03/22

# ejemplo poo

class Persona():
    # Atributos de clase
    nombre = 'Sonia'
    apellidos : str
    edad = 0
    email = 'sonia.garciam@pfsgroup.es'

    # Constructor de clase que queramos pasar si o si para la clase
    def __init__(self, newNom, newApe):
        self.nombre = newNom
        self.apellidos = newApe

    # Comportamiento - metodos de clase

    def saludar(self):
        print(f'Bienbenido {self.nombre}')


# Autor: Sonia Garcia
# version: 0.0.1
# data: 09/03/2022

from poo.Persona import Persona
from poo.Alumno import Alumno
from club.Player import Player
from club.Team import Team

# if __name__ == '__main__':
#     p1 = Persona('Pedro','Gomez') # Instancia de clase
#     p2 = Persona('Luis','Perez') # Instancia de clase
#     print(p1)
#     print(p1.nombre)
#     print(f'Bienvenido {p1.nombre} {p1.apellidos}')
#     print(p1.edad)
#     p1.edad = 25
#     print(p1.edad)
#     p1.saludar()
#     print(p1.nombre, p1.apellidos)

if __name__ == '__main__':
    a1 = Alumno('Juan','Garcia','48575659L',27)
    a2 = Alumno('Alba','Garcia','47889875A',50)

    a1.nota(50)

    j = Player('Pepe', 20, 'portero')
    print(j)

    j.saluda()

    team1 = Team()
    team1.addPlayer(j)
    team1.getPlayers()
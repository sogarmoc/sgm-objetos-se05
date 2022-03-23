# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 15/03/22

class Team():
    # Atributos de clase
    players = []

    # Constructor de clase
    def __init__(self):
        pass

    # Metodos de clase -  comportamiento

    def addPlayer(self, newPlayer):
        self.players.append(newPlayer)
        print(f'Nuevo jugador')

    def getPlayers(self):
        print(self.players[0])
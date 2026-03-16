class Helicopter:
    def __init__(self, fuselage, rotor, tail):
        self.fuselage = fuselage
        self.rotor = rotor
        self.tail = tail
        self.antennas = []

    def add_antenna(self, antenna):
        self.antennas.append(antenna)

    def geometry_mesh(self):
        # retourne le mesh conducteur
        pass
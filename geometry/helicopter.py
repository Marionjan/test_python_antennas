import pyvista as pv
import numpy as np

class Helicopter:
    def __init__(self, fuselage, rotor, tail):
        self.fuselage = fuselage
        self.rotor = rotor
        self.tail = tail
        self.antennas = []

    def add_antenna(self, antenna):
        self.antennas.append(antenna)

    def geometry_mesh(self):
        # fuselage = cylindre
        fuselage_mesh = pv.Cylinder(
            center=(0, 0, 0),
            direction=(1, 0, 0),
            radius=self.fuselage.radius,
            height=self.fuselage.length
        )

        # rotor = disque simple
        rotor_mesh = pv.Disc(
            center=(0, 0, self.fuselage.radius),
            inner=0,
            outer=self.rotor.blade_length
        )

        return fuselage_mesh + rotor_mesh
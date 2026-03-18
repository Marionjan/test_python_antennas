import pyvista as pv
import numpy as np

class Helicopter:
    def __init__(self, fuselage, rotor, back_rotor, tail, nose):
        self.fuselage = fuselage
        self.rotor = rotor
        self.back_rotor = back_rotor
        self.tail = tail
        self.nose = nose
        self.antennas = []

    def add_antenna(self, antenna):
        self.antennas.append(antenna)
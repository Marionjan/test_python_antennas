import numpy as np

class IsotropicAntenna(Antenna):
    def __init__(self, position, orientation, frequency, gain_dbi=0):
        super().__init__(position, orientation, frequency)
        self.gain_dbi = gain_dbi  # gain en dBi

    def radiation_pattern(self, theta, phi):
        """
        Antenne isotrope → gain constant dans toutes les directions.
        Retourne le gain en linéaire.
        """
        gain_linear = 10 ** (self.gain_dbi / 10)
        return gain_linear
from antennas.antenna import Antenna


class Monopole(Antenna):
    
    def radiation_pattern(self, theta, phi):
        import numpy as np
        return np.sin(theta)
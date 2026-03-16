import numpy as np

from antennas.antenna import Antenna
from utils.constants import C
from utils.math_utils import normalize


class Dipole(Antenna):
    """
    Simple dipole antenna model.
    """

    def __init__(self, position, orientation, frequency, tx_power_dBm, length=None):
        """
        Parameters
        ----------
        position : list or array [x,y,z]
        orientation : vector direction of dipole
        frequency : Hz
        length : dipole length (optional)
        """

        super().__init__(position, orientation, frequency, tx_power_dBm)

        self.orientation = normalize(orientation)
        self.gain = 1

        # default : half-wave dipole
        if length is None:
            self.length = C / (2 * frequency)
        else:
            self.length = length

    def radiation_pattern(self, theta, phi):
        """
        Radiation pattern of a dipole antenna.

        Parameters
        ----------
        theta : polar angle
        phi : azimuth angle

        Returns
        -------
        field magnitude
        """

        # classic dipole pattern
        return np.sin(theta)

    def gain(self, theta):
        """
        Approximate gain pattern.
        """

        return np.sin(theta) ** 2

    def __repr__(self):

        return (
            f"Dipole(position={self.position}, "
            f"orientation={self.orientation}, "
            f"frequency={self.frequency/1e6:.1f} MHz)"
        )
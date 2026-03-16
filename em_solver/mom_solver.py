import numpy as np

from utils.constants import C, PI
from utils.math_utils import distance


class MoMSolver:
    """
    Simplified Method of Moments solver.

    This solver approximates coupling between antennas
    using radiated field propagation and phase delay.
    """

    def __init__(self, helicopter):
        self.heli = helicopter

    def wavenumber(self, frequency):
        """
        k = 2π / λ
        """
        wavelength = C / frequency
        return 2 * PI / wavelength

    def compute_field(self, antenna, observation_point):
        """
        Compute electric field emitted by an antenna
        at a given observation point.

        Uses a simplified spherical wave model.
        """

        antenna_pos = np.array(antenna.position, dtype=float)

        if isinstance(observation_point, (tuple, list)) and len(observation_point) == 3:
            # observation_point is a 3D meshgrid (X, Y, Z)
            x, y, z = observation_point
            r = np.sqrt(
                (x - antenna_pos[0]) ** 2
                + (y - antenna_pos[1]) ** 2
                + (z - antenna_pos[2]) ** 2
            )
        else:
            r = distance(antenna_pos, observation_point)

            if r == 0:
                return 0

        freq = antenna.frequency
        k = self.wavenumber(freq)

        # spherical wave approximation
        phase = np.exp(-1j * k * r)

        if np.isscalar(r):
            E = phase / r
        else:
            E = np.zeros_like(r, dtype=complex)
            np.divide(phase, r, out=E, where=r != 0)

        return E

    def compute_coupling(self, antenna_tx, antenna_rx):
        """
        Estimate coupling coefficient between two antennas.

        Returns
        -------
        complex number approximating S21
        """

        r = distance(antenna_tx.position, antenna_rx.position)

        if r == 0:
            return 1

        freq = antenna_tx.frequency
        k = self.wavenumber(freq)

        # radiation pattern influence
        theta = np.pi / 2
        phi = 0

        G_tx = antenna_tx.radiation_pattern(theta, phi)
        G_rx = antenna_rx.radiation_pattern(theta, phi)

        # spherical wave propagation
        coupling = G_tx * G_rx * np.exp(-1j * k * r) / (4 * PI * r)

        return coupling
import numpy as np

class EMSolver:

    def __init__(self, geometry):
        self.geometry = geometry

    def compute_field(self, antenna, observation_point):
        r = np.linalg.norm(observation_point - antenna.position)
        if r == 0:
            return 0
        return np.exp(-1j * 2*np.pi * antenna.frequency * r) / r

    def compute_coupling(self, antenna_tx, antenna_rx):
        d = np.linalg.norm(antenna_tx.position - antenna_rx.position)
        if d == 0:
            return 1+0j
        return np.exp(-1j * d) / d
"""
Physical constants used in the RF helicopter simulator.
All values are in SI units.
"""

import numpy as np

# Speed of light in vacuum (m/s)
C = 299792458

# Vacuum permittivity (F/m)
EPSILON_0 = 8.854187817e-12

# Vacuum permeability (H/m)
MU_0 = 4 * np.pi * 1e-7

# Free space impedance (Ohms)
Z0 = np.sqrt(MU_0 / EPSILON_0)

# Pi constant
PI = np.pi
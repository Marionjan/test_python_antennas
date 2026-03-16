import numpy as np


def compute_near_field(grid, antennas, solver):
    X, _, _ = grid

    field = np.zeros_like(X, dtype=complex)

    for ant in antennas:
        field += solver.compute_field(ant, grid)

    return field
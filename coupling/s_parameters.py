import numpy as np

def compute_coupling_matrix(antennas, solver):

    n = len(antennas)
    S = np.zeros((n,n), dtype=complex)

    for i in range(n):
        for j in range(n):
            S[i,j] = solver.compute_coupling(
                antennas[i],
                antennas[j]
            )

    return S
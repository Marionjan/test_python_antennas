import matplotlib.pyplot as plt
import numpy as np

def plot_coupling_matrix(S):

    S_db = 20 * np.log10(np.abs(S) + 1e-12)

    plt.figure()
    plt.imshow(S_db, cmap="viridis")
    plt.colorbar(label="|Sij| (dB)")
    plt.title("Coupling Matrix")
    plt.xlabel("Tx antenna")
    plt.ylabel("Rx antenna")
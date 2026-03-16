import matplotlib.pyplot as plt
import numpy as np

def plot_field_slice(field, grid, axis="z", index=None):
    X, Y, Z = grid
    E = np.abs(np.asarray(field))

    if axis == "z":
        if index is None:
            index = Z.shape[2] // 2
        Xs = X[:, :, index]
        Ys = Y[:, :, index]
        Es = E[:, :, index]
        slice_label = f"z = {Z[0, 0, index]:.2f}"
    elif axis == "y":
        if index is None:
            index = Y.shape[1] // 2
        Xs = X[:, index, :]
        Ys = Z[:, index, :]
        Es = E[:, index, :]
        slice_label = f"y = {Y[0, index, 0]:.2f}"
    elif axis == "x":
        if index is None:
            index = X.shape[0] // 2
        Xs = Y[index, :, :]
        Ys = Z[index, :, :]
        Es = E[index, :, :]
        slice_label = f"x = {X[index, 0, 0]:.2f}"
    else:
        raise ValueError("axis must be one of: 'x', 'y', 'z'")

    plt.figure()
    plt.contourf(Xs, Ys, Es, levels=40)
    plt.colorbar(label="|E|")
    plt.title(f"Near Field Magnitude ({slice_label})")
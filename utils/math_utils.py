import numpy as np


def create_3d_grid(xlim, ylim, zlim, resolution):
    """
    Create a 3D grid of points.

    Parameters
    ----------
    xlim : tuple (xmin, xmax)
    ylim : tuple (ymin, ymax)
    zlim : tuple (zmin, zmax)
    resolution : int
        Number of points per axis

    Returns
    -------
    X, Y, Z : ndarray
        Meshgrid arrays
    """

    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    z = np.linspace(zlim[0], zlim[1], resolution)

    X, Y, Z = np.meshgrid(x, y, z)

    return X, Y, Z


def distance(p1, p2):
    """
    Euclidean distance between two points.
    """

    p1 = np.array(p1)
    p2 = np.array(p2)

    return np.linalg.norm(p1 - p2)


def normalize(v):
    """
    Normalize a vector.
    """

    v = np.array(v)
    norm = np.linalg.norm(v)

    if norm == 0:
        return v

    return v / norm


def spherical_coordinates(x, y, z):
    """
    Convert Cartesian coordinates to spherical coordinates.

    Returns
    -------
    r, theta, phi
    """

    r = np.sqrt(x**2 + y**2 + z**2)

    theta = np.arccos(z / (r + 1e-12))
    phi = np.arctan2(y, x)

    return r, theta, phi


def wavelength(frequency, c=299792458):
    """
    Compute wavelength from frequency.

    λ = c / f
    """

    return c / frequency
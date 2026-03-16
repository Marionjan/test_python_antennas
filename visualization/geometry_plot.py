import matplotlib.pyplot as plt
import numpy as np

from visualization.ax import set_axes_equal
from visualization.radiation_plot import plot_3d_radiation_pattern


def plot_helicopter(heli):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # fuselage (cylindre simplifié)
    Lf = heli.fuselage.length
    Rf = heli.fuselage.radius
    
    xf1 = np.linspace(-Lf/2, Lf/2, 50)
    theta1 = np.linspace(0, 2*np.pi, 50)
    theta, xf = np.meshgrid(theta1, xf1)

    y = Rf * np.cos(theta)
    z = Rf * np.sin(theta)
    
    ax.plot_surface(xf, y, z, alpha=0.3, color = "cyan")

    # tail (cylindre simplifié)
    Lt = heli.tail.length
    Rt = heli.tail.radius
    
    xt1 = np.linspace(-Lf/2, -(Lf/2 + Lt), 50)
    theta, xt = np.meshgrid(theta1, xt1)

    y = Rt * np.cos(theta)
    z = Rt * np.sin(theta)

    ax.plot_surface(xt, y, z, alpha=0.3)
    
    # antennes
    for ant in heli.antennas:
        p = ant.position
        ax.scatter(p[0], p[1], p[2], color='red', s=40)
        xant, yant, zant = plot_3d_radiation_pattern(ant)
        # fig = plt.gcf()
        # ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(xant, yant, zant, alpha = 1,cmap='viridis' )         #cmap='viridis'

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    set_axes_equal(ax)

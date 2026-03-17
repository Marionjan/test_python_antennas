from visualization.radiation_plot import plot_3d_radiation_pattern
import pyvista as pv
import numpy as np


def plot_helicopter(heli):

    plotter = pv.Plotter()

    # ======================
    # FUSELAGE
    # ======================
    Lf = heli.fuselage.length
    Rf = heli.fuselage.radius

    fuselage = pv.Cylinder(
        center=(0, 0, 0),
        direction=(1, 0, 0),
        radius=Rf,
        height=Lf,
        resolution=50
    )

    plotter.add_mesh(fuselage, color="cyan", opacity=0.3)

    # ======================
    # TAIL
    # ======================
    if heli.tail is not None:
        Lt = heli.tail.length
        Rt = heli.tail.radius

        tail = pv.Cylinder(
            center=(-Lf/2 - Lt/2, 0, 0),
            direction=(1, 0, 0),
            radius=Rt,
            height=Lt,
            resolution=50
        )

        plotter.add_mesh(tail, color="lightgray", opacity=0.3)

    # ======================
    # ANTENNES
    # ======================
    for ant in heli.antennas:
        p = ant.position

        # point antenne
        antenna_point = pv.Sphere(radius=0.1, center=p)
        plotter.add_mesh(antenna_point, color="red")

        # ======================
        # RAYONNEMENT
        # ======================
        try:
            xant, yant, zant = plot_3d_radiation_pattern(ant)

            points = np.c_[xant.ravel(), yant.ravel(), zant.ravel()]
            radiation = pv.PolyData(points)

            field = np.sqrt(xant**2 + yant**2 + zant**2)

            radiation["gain"] = field.ravel(order="F")

            plotter.add_mesh(
                radiation,
                scalars="gain",
                cmap="viridis",
                opacity=1
            )
        except Exception:
            pass  # si pas défini

    # ======================
    # AFFICHAGE
    # ======================
    # plotter.add_axes()
    plotter.add_title("Helicopter + Antennas")
    plotter.show()
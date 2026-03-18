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

    plotter.add_mesh(fuselage, color="lightgray", opacity=1)

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

        plotter.add_mesh(tail, color="lightgray", opacity=1)
        
    # ======================
    # NOSE
    # ======================
    if heli.nose is not None:
        base_radius = heli.nose.radius
        nose_height = heli.nose.height

        nose = pv.Cone(
            center=(Lf/2 + nose_height/2, 0, 0),
            direction=(1, 0, 0),
            radius=base_radius,
            height=nose_height,
            resolution= 18
        )
        plotter.add_mesh(nose, color="lightgray", opacity=1)
        
        bottom = pv.Cone(
            center=(-Lf/2 - nose_height/2, 0, 0),
            direction=(-1, 0, 0),
            radius=base_radius,
            height=nose_height,
            resolution= 18
        )
        plotter.add_mesh(bottom, color="lightgray", opacity=1)
        
        
    # ======================
    # ROTORS
    # ======================
    if heli.rotor is not None:
        rotor = pv.Disc(
            center=(0, 0, heli.fuselage.radius + 0.2),
            inner=0,
            outer=heli.rotor.blade_length,
            c_res = 18
        )

        plotter.add_mesh(rotor, color="cyan", opacity=0.3)
        
    if heli.back_rotor is not None:
        back_rotor = pv.Disc(
        center=(-Lf/2 - Lt, -0.5, Rt/2 + 0.5),
        normal=(0, 1, 0),
        inner=0,
        outer=heli.back_rotor.blade_length,
        c_res = 18
    )

    plotter.add_mesh(back_rotor, color="cyan", opacity=0.3)

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

            field = np.sqrt((xant - p[0])**2 + (yant - p[1])**2 + (zant - p[2])**2)
            radiation["gain"] = field.ravel(order="F")

            plotter.add_mesh(
                radiation,
                scalars="gain",
                cmap="viridis",
                opacity=1,
            )
        except Exception:
            pass  # si pas défini

    # ======================
    # AFFICHAGE
    # ======================
    plotter.add_title("Helicopter + Antennas")
    plotter.show()
# =========================
# Standard libraries
# =========================
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Geometry
# =========================
from geometry.helicopter import Helicopter
from geometry.fuselage import Fuselage
from geometry.rotor import Rotor
from geometry.tail import Tail

# =========================
# Antennas
# =========================
from antennas.dipole import Dipole
from antennas.monopole import Monopole
# from antennas.patch import Patch

# =========================
# Electromagnetic solver
# =========================
from em_solver.mom_solver import MoMSolver
# from em_solver.fdtd_solver import FDTDSolver

# =========================
# Coupling computation
# =========================
from coupling.coupling_matrix import compute_coupling_matrix
# from coupling.s_parameters import compute_s_parameters

# =========================
# Field propagation
# =========================
from propagation.near_field import compute_near_field
# from propagation.far_field import compute_far_field

# =========================
# Optimization
# =========================
# from optimization.antenna_placement import optimize_antenna_positions
# from optimization.cost_functions import coupling_cost

# =========================
# Visualization
# =========================
from visualization.geometry_plot import plot_helicopter
from visualization.field_plot import plot_field_slice
from visualization.coupling_plot import plot_coupling_matrix
from visualization.radiation_plot import plot_radiation_pattern


# =========================
# Utilities
# =========================
from utils.constants import C
from utils.math_utils import create_3d_grid


def main():

    # -------------------------
    # 1. Create helicopter geometry
    # -------------------------
    fuselage = Fuselage(length=8.2, radius=1, conductivity=5.8e7)
    rotor = Rotor(n_blades=6, blade_length=8, angular_speed=30)
    tail = Tail(length=11.3, radius=0.4)

    heli = Helicopter(fuselage, rotor, tail)

    # -------------------------
    # 2. Add antennas
    # -------------------------
    """    
    x: AVANT - ARRIERE
    y: DROITE - GAUCHE
    z: HAUT - BAS
    """
    ant1 = Dipole(position=[4.1, 0, 0], orientation=[1, 0, 0], frequency=88e6)
    ant2 = Dipole(position=[-6, 0, 0.4], orientation=[0, 0, 1], frequency=88e6)
    ant3 = Dipole(position=[-5, 0, 0.4], orientation=[0, 0, 1], frequency=88e6)
    
    # Antennes tests
    # ant1 = Dipole(position=[0, 0, 0], orientation=[0, 0, 0], frequency=88e6)
    # ant2 = Dipole(position=[2, 0, 0], orientation=[0, 0, 1], frequency=88e6)
    # ant3 = Dipole(position=[4, 0, 0], orientation=[0, 1, 0], frequency=88e6)
    # ant4 = Dipole(position=[6, 0, 0], orientation=[0, 1, 1], frequency=88e6)
    # ant5 = Dipole(position=[8, 0, 0], orientation=[1, 0, 0], frequency=88e6)
    # ant6 = Dipole(position=[10, 0, 0], orientation=[1, 0, 1], frequency=88e6)
    # ant7 = Dipole(position=[12, 0, 0], orientation=[1, 1, 0], frequency=88e6)
    # ant8 = Dipole(position=[14, 0, 0], orientation=[1, 1, 1], frequency=88e6)



    heli.add_antenna(ant1)
    heli.add_antenna(ant2)
    heli.add_antenna(ant3)
    # heli.add_antenna(ant4)
    # heli.add_antenna(ant5)
    # heli.add_antenna(ant6)
    # heli.add_antenna(ant7)
    # heli.add_antenna(ant8)
    
    # -------------------------
    # 3. Visualization
    # -------------------------
    plot_helicopter(heli)

    # -------------------------
    # 4. Create EM solver
    # -------------------------
    solver = MoMSolver(heli)

    # -------------------------
    # 5. Compute coupling matrix
    # -------------------------
    S = compute_coupling_matrix(heli.antennas, solver)

    print("Coupling matrix S:")
    print(S)

    # -------------------------
    # 6. Plot coupling
    # -------------------------
    plot_coupling_matrix(S)

    # -------------------------
    # 7. Near field simulation
    # -------------------------
    # grid = create_3d_grid(xlim=(-10,10), ylim=(-10,10), zlim=(0,10), resolution=20)

    # field = compute_near_field(grid, heli.antennas, solver)

    # plot_field_slice(field, grid)

    plt.show()


if __name__ == "__main__":
    main()
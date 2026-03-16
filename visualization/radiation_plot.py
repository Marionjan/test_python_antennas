import numpy as np
import matplotlib.pyplot as plt

def plot_radiation_pattern(antenna):

    theta = np.linspace(0, np.pi, 200)
    gain = antenna.radiation_pattern(theta, 0)

    plt.figure()
    plt.polar(theta, np.abs(gain))
    plt.title("Radiation Pattern")
    
def plot_3d_radiation_pattern(antenna):
    
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    theta_grid, phi_grid = np.meshgrid(theta, phi)

    gain = antenna.gain(theta_grid, phi_grid)
    gain_abs = np.abs(gain)

    # Convert spherical to cartesian coordinates
    x = gain_abs * np.sin(theta_grid) * np.cos(phi_grid)
    y = gain_abs * np.sin(theta_grid) * np.sin(phi_grid)
    z = gain_abs * np.cos(theta_grid)

    # Apply orientation rotation
    orientation = np.array(antenna.orientation)
    orientation = orientation / np.linalg.norm(orientation)
    # Find rotation axis and angle from [0,0,1] to orientation
    z_axis = np.array([0, 0, 1])
    axis = np.cross(z_axis, orientation)
    angle = np.arccos(np.dot(z_axis, orientation))
    if np.linalg.norm(axis) != 0:
        axis = axis / np.linalg.norm(axis)
        # Rodrigues' rotation formula
        K = np.array([[0, -axis[2], axis[1]],
                      [axis[2], 0, -axis[0]],
                      [-axis[1], axis[0], 0]])
        I = np.eye(3)
        R = I + np.sin(angle) * K + (1 - np.cos(angle)) * np.dot(K, K)
        xyz = np.stack([x, y, z], axis=-1)
        xyz_rot = np.tensordot(xyz, R, axes=([2],[1]))
        x_rot, y_rot, z_rot = xyz_rot[...,0], xyz_rot[...,1], xyz_rot[...,2]
    else:
        x_rot, y_rot, z_rot = x, y, z

    # Add antenna position
    x_rot = x_rot + antenna.position[0]
    y_rot = y_rot + antenna.position[1]
    z_rot = z_rot + antenna.position[2]

    return x_rot, y_rot, z_rot

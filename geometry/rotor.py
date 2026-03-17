import numpy as np

class Rotor:
    def __init__(self, n_blades, blade_length, angular_speed):
        self.n_blades = n_blades
        self.blade_length = blade_length
        self.omega = angular_speed

    def blade_positions(self, t):
        angles = [
            2*np.pi*i/self.n_blades + self.omega*t
            for i in range(self.n_blades)
        ]

        return [
            (self.blade_length*np.cos(a),
             self.blade_length*np.sin(a),
             0)
            for a in angles
        ]
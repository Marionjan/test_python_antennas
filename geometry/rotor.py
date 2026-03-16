class Rotor:
    def __init__(self, n_blades, blade_length, angular_speed):
        self.n_blades = n_blades
        self.blade_length = blade_length
        self.omega = angular_speed

    def blade_positions(self, t):
        # position des pales à l'instant t
        pass
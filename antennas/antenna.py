class Antenna:
    def __init__(self, position, orientation, frequency):
        self.position = position
        self.orientation = orientation
        self.frequency = frequency

    def radiation_pattern(self, theta, phi):
        raise NotImplementedError
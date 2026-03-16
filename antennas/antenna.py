class Antenna:
    def __init__(self, position, orientation, frequency, gain, tx_power_dBm):
        self.position = position
        self.orientation = orientation
        self.frequency = frequency
        self.gain = gain
        self.tx_power_dBm = tx_power_dBm

    def radiation_pattern(self, theta, phi):
        raise NotImplementedError
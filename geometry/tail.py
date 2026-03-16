import numpy as np


class Tail:
    """
    Simplified helicopter tail model.

    The tail is modeled as a conductive cylinder.
    """

    def __init__(self, length, radius, conductivity=5.8e7, position=None, direction=None):
        """
        Parameters
        ----------
        length : float
            Length of the tail (meters)
        radius : float
            Radius of the tail cylinder (meters)
        conductivity : float
            Electrical conductivity (S/m)
        position : list [x,y,z]
            Base position of the tail
        direction : list [dx,dy,dz]
            Direction vector of the tail
        """

        self.length = length
        self.radius = radius
        self.conductivity = conductivity

        if position is None:
            self.position = np.array([0, 0, 0])
        else:
            self.position = np.array(position)

        if direction is None:
            self.direction = np.array([1, 0, 0])
        else:
            self.direction = np.array(direction)

    def get_axis_points(self):
        """
        Returns the start and end points of the tail axis.
        """

        start = self.position
        end = self.position + self.direction * self.length

        return start, end

    def __repr__(self):

        return (
            f"Tail(length={self.length}, "
            f"radius={self.radius}, "
            f"position={self.position.tolist()})"
        )
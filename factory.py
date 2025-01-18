"""Module that has factories for tuples and matrices."""

def point(x, y, z):
    """Creates a point with w = 1.0."""
    return (x, y, z, 1.0)

def vector(x, y, z):
    """Creates a vector with w = 0.0."""
    return (x, y, z, 0.0)

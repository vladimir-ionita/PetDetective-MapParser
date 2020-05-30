def distance_between_points(p1, p2):
    """Calculate the distance between two points.

    Parameters:
        p1 (tuple of int): coordinates of the first point
        p2 (tuple of int): coordinates of the second point

    Returns:
        int: the distance between the points
    """
    import math

    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


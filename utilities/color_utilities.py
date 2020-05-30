def make_color_range(color, delta):
    """Return a color range based on a color and a variation.

    Parameters:
        color (list of int): the RGB color
        delta (int): the variation for the range

    Returns:
        tuple of list of int: tuple representing the color range (lower and upper boundary)
    """
    return list(map(lambda x: x-delta, color)), list(map(lambda x: x+delta, color))

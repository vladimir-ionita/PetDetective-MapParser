import cv2
import numpy as np
import math


def detect_intersection_nodes(image, intersection_node_image):
    locations = cv2.matchTemplate(image, intersection_node_image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(locations >= 0.9)

    coordinates_split = locations[::-1]
    coordinates = list(zip(*coordinates_split))

    node_coordinates = [coordinates.pop(0)]
    for coord in coordinates:
        if coordinates_far_enough(coord, node_coordinates):
            node_coordinates.append(coord)
    return node_coordinates


def coordinates_far_enough(coordinates, all_coordinates):
    for coord in all_coordinates:
        if distance_between_points(coord, tuple(coordinates)) < 20:
            return False
    return True


def distance_between_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


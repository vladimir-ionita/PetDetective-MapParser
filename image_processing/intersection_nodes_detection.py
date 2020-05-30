import cv2
import numpy as np
from geometry.line_segment.utilities import distance_between_points


BEST_MATCHES_PROBABILITY = 0.9
DISTANCE_THRESHOLD = 20


def get_intersection_nodes_coordinates(image, intersection_node_image):
    """Finds intersection node coordinates based on intersection node image.
    The method uses template matching to find the coordinates.

    Parameters:
        image (image): the image on which the search is performed
        intersection_node_image (image): the template image to search for matches

    Returns:
         list of tuples of int: list of (x, y) coordinates representing the intersection nodes
    """
    # Find subimage matching probabilities in the image
    subimage_locations_probabilities = cv2.matchTemplate(image, intersection_node_image, cv2.TM_CCOEFF_NORMED)

    # Get locations of most probable matches
    best_match_locations = np.where(subimage_locations_probabilities >= BEST_MATCHES_PROBABILITY)

    # Switch columns and rows to get the x and y coordinates in order
    best_match_locations_split_coordinates = best_match_locations[::-1]

    # Merge the lists of x and y to create best matches coordinates
    best_match_locations_coordinates = list(zip(*best_match_locations_split_coordinates))

    # Filter out coordinates related to the same intersection
    intersection_node_coordinates = [best_match_locations_coordinates.pop(0)]
    for location_coordinates in best_match_locations_coordinates:
        if are_coordinates_far_enough_to_form_an_intersection_alone(location_coordinates, intersection_node_coordinates):
            intersection_node_coordinates.append(location_coordinates)
    return intersection_node_coordinates


def are_coordinates_far_enough_to_form_an_intersection_alone(coordinates, all_coordinates):
    """Checks if coordinates are far enough to form an intersection or is part of an existing intersection.

    Parameters:
        coordinates (tuple of int): the coordinates to be checked
        all_coordinates (list of tuple of int): all intersection coordinates

    Returns:
        bool: True if the coordinates can form an intersection and False if it is part of another intersection.
    """
    for coord in all_coordinates:
        if distance_between_points(coord, tuple(coordinates)) < DISTANCE_THRESHOLD:
            return False
    return True

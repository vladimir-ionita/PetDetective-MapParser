import cv2
import numpy as np
from utilities.color_utilities import *


CONTOUR_AREA_THRESHOLD = 100
INTERSECTION_NODE_COLOR_RANGE_DELTA = 1
CONTOUR_DRAWING_COLOR = (0, 255, 0)     # Green
CONTOUR_DRAWING_LINE_THICKNESS = 3


def get_intersection_nodes_coordinates_v2(image, intersection_node_color, center_coordinates=False):
    """Finds intersection node coordinates based on intersection node color.
    The method uses contour finding to find the coordinates.

    Parameters:
        image (image): the image on which the search is performed
        intersection_node_color (list of int): the color to search for
        center_coordinates (bool): a flag to indicate whether to search for the intersection node coordinates or
                                   the center of the intersection node

    Returns:
        list of tuples of int: list of (x, y) coordinates representing the intersection nodes
    """
    # Create a color range
    intersection_node_color_range = make_color_range(intersection_node_color, INTERSECTION_NODE_COLOR_RANGE_DELTA)

    # Create lower and upper color boundaries
    lower_color_boundary = np.array(intersection_node_color_range[0], dtype="uint8")
    upper_color_boundary = np.array(intersection_node_color_range[1], dtype="uint8")

    # Threshold image with the color boundaries
    thresholded_image = cv2.inRange(image, lower_color_boundary, upper_color_boundary)

    # Find the groupings of pixels
    contours, hierarchy = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find contours with a big enough area to be an intersection node
    intersection_nodes_contours = []
    for c in contours:
        contour_area = cv2.contourArea(c)
        if contour_area > CONTOUR_AREA_THRESHOLD:
            intersection_nodes_contours.append(c)

    # Draw contours on the original image (illustration purpose only)
    # draw_contours(image, intersection_nodes_contours, 'resources/result.png')

    # Find intersection nodes coordinates
    intersection_nodes_coordinates = []
    if center_coordinates:
        for c in intersection_nodes_contours:
            # Get the center of the contour
            contour_moments = cv2.moments(c)
            contour_center_x = int(contour_moments["m10"] / contour_moments["m00"])
            contour_center_y = int(contour_moments["m01"] / contour_moments["m00"])
            intersection_nodes_coordinates.append((contour_center_x, contour_center_y))
    else:
        for c in intersection_nodes_contours:
            # Get the first (random) coordinate of the contour.
            # Every coordinate of the contour represents the intersection node.
            intersection_nodes_coordinates.append(c[0][0])

    return intersection_nodes_coordinates


def draw_contours(image, contours, file_path):
    """Draws the contours on an image and writes the image to a file.

    Parameters:
        image (image): the image to draw contours on
        contours (list of contour): the contours to draw
        file_path (str): the file path to write the image to
    """
    cv2.drawContours(image, contours, -1, CONTOUR_DRAWING_COLOR, CONTOUR_DRAWING_LINE_THICKNESS)
    cv2.imwrite(file_path, image)

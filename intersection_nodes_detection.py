import cv2
import numpy as np
import math


def detect_intersection_nodes(image, intersection_node_image):
    locations = cv2.matchTemplate(image, intersection_node_image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(locations >= 0.9)

    coordinates_split = locations[::-1]
    coordinates = list(zip(*coordinates_split))
    

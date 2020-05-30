from image_processing.intersection_nodes_detection_v2 import get_intersection_nodes_coordinates_v2
from image_processing.intersection_nodes_detection import get_intersection_nodes_coordinates
import constants
import cv2


if __name__ == "__main__":
    map_image = cv2.imread("resources/maps/IMG_9931.PNG")
    intersection_node_image = cv2.imread("resources/map_parts/intersection.png")

    nodes = get_intersection_nodes_coordinates(map_image, intersection_node_image)
    nodes.sort()
    print(nodes)
    nodes = get_intersection_nodes_coordinates_v2(map_image, constants.Colors.intersection_node_color, True)
    nodes.sort()
    print(nodes)

from intersection_nodes_detection import *
import cv2


if __name__ == "__main__":
    map_image = cv2.imread("resources/maps/IMG_9931.PNG")
    intersection_node_image = cv2.imread("resources/map_parts/intersection.png")

    nodes = detect_intersection_nodes(map_image, intersection_node_image)
    print(nodes)


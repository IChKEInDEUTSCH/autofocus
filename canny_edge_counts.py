import cv2 as cv
import sys
import numpy as np

def canny_edge_counts(argv):
    if len(argv) == 1:
        # Load the image
        src = cv.imread(argv[0], cv.IMREAD_COLOR)
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image: ' + argv[0])
            return -1
    elif len(argv) == 0:
        print ('Not enough parameters')
        print ('Usage:/nmorph_lines_detection.py < path_to_image >')
        return -1
    else:
        src = argv[0]

    canny = cv.Canny(src, 255/3, 255)

    to_nparray = np.array(canny)
    total_zeros_count = to_nparray[np.where(to_nparray==255)].size

    return total_zeros_count

if __name__ == "__main__":
    canny_edge_counts(sys.argv[1:])
    
import cv2 as cv
import sys
import numpy as np

def sobel_edge_counts(argv):
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    
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
        src = argv
    
    grad_x = cv.Sobel(src, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    # Gradient-Y
    # grad_y = cv.Scharr(gray,ddepth,0,1)
    grad_y = cv.Sobel(src, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    to_nparray = np.array(grad)
    total_zeros_count = to_nparray[np.where(to_nparray==255)].size

    return total_zeros_count

if __name__ == "__main__":
    sobel_edge_counts(sys.argv[1:])
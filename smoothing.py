import cv2 as cv
import sys

def bilateral_blur(argv,int_d = 5,int_colorSigma = 11,int_spaceSigma = 11):
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

    src = cv.bilateralFilter(src, int_d, int_colorSigma, int_spaceSigma)

    return src

def gaussian_blur(argv,ksize = 3):
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

    src = cv.GaussianBlur(src, (ksize,ksize),cv.BORDER_CONSTANT)

    return src

if __name__ == "__main__":
    bilateral_blur(sys.argv[1:])
    gaussian_blur(sys.argv[1:])
    
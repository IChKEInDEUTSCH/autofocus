import cv2 as cv
import sys
import canny_edge_counts as cec
import smoothing as smooth

def autofocus(argv):

    if len(argv) == 1:
        # Load the video
        src = cv.VideoCapture(argv[0])
        # Check if video is loaded fine
        if not src.isOpened():
            print ('Error opening vid: ' + argv[0])
            return -1
    elif len(argv) == 0:
        print ('Not enough parameters')
        print ('Usage:/nautofocus.py < path_to_vid >')
        return -1
    else:
        src = argv[0]
    retval = True
    highest_edge_counts = 0
    while src.isOpened():
        retval, frame = src.read()
        if not retval:
            print('Stream end')
            break
        blur =  smooth.bilateral_blur(frame,5,3,3)
        gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
        counts = cec.canny_edge_counts(gray)

        if counts > highest_edge_counts:
            best_frame = frame
            highest_edge_counts = counts
    src.release()
    cv.imshow('best focal view', best_frame)
    cv.waitKey(0)
    return 0

if __name__ == "__main__":
    autofocus(sys.argv[1:])
    
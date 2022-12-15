from skimage.exposure import is_low_contrast
import cv2

def is_having_low(image, thres_hold):
    # image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if is_low_contrast(gray, fraction_threshold= thres_hold):
        return False
    else:
        return True

    # cv2.imshow("Detection Output", im)
    # cv2.waitKey(0)
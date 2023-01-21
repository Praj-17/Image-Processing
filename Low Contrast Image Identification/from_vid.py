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

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('output.avi', 
                        cv2.VideoWriter_fourcc(*'MJPG'),
                        10, size)

while True:
    ret, frame = cam.read()
    frame = is_having_low(frame, fraction = 0.5)
    
    cv2.imshow("Detection Output", frame)
    result.write(frame)
                    
                    #Terminate while loop of q key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cam.release()
result.release()
cv2.destroyAllWindows()
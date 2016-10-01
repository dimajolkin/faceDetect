import cv2
import numpy as np
import sys
import os.path

cascPath = '/root/opencv/data/haarcascades/haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(1)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

print "hello"
if not os.path.isfile(cascPath):
    print "file not exist " + cascPath
    exit()

def rotateImage(image, angle):
    image0 = image
    if hasattr(image, 'shape'):
        image_center = tuple(np.array(image.shape)/2)
        shape = tuple(image.shape)
    elif hasattr(image, 'width') and hasattr(image, 'height'):
        image_center = tuple(np.array((image.width/2, image.height/2)))
        shape = (image.width, image.height)
    else:
        raise Exception, 'Unable to acquire dimensions of image for type %s.' % (type(image),)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    image = np.asarray( image[:,:] )

    rotated_image = cv2.warpAffine(image, rot_mat, shape, flags=cv2.INTER_LINEAR)

    # Copy the rotated data back into the original image object.
    cv2.SetData(image0, rotated_image.tostring())

    return image0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        centerX = x + (w / 2)
        centerY = y + (h / 2)
        center = (centerX, centerY)
        cv2.circle(frame, center, 10, color=(0, 0, 255))
        print center

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
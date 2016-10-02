import cv2
import os

from arduino import Arduino

arduino = Arduino()
arduino.connect()

cascPath = os.path.dirname(os.path.abspath(__file__))  + '/data/haarcascade_frontalface_alt.xml'
print "hello"
if not os.path.isfile(cascPath):
    print "file not exist " + cascPath
    exit()

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_COUNT, 10)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    cv2.flip(frame, 1, frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    height, width, channels = frame.shape

    cv2.line(frame, (width / 2, 0), (width / 2, height), color=(0, 0, 255))

    if len(faces) == 0:
        arduino.push("0 0")

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        centerX = x + (w / 2)
        centerY = y + (h / 2)
        center = (centerX, centerY)

        cv2.circle(frame, center, 20, color=(0, 0, 255))

        if x < width /2 and x + w > width / 2:
            push_x = 0
        elif width / 2 > centerX:
            push_x = -1
        else:
            push_x = 1

        if y < height /2 and y + h > height / 2:
            push_y = 0
        elif height / 2 > centerY:
            push_y = 1
        else:
            push_y = -1

        arduino.push("{0} {1}".format(push_x, push_y))
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
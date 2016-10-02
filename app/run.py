import cv2
import os

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

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        centerX = x + (w / 2)
        centerY = y + (h / 2)
        center = (centerX, centerY)
        cv2.circle(frame, center, 10, color=(0, 0, 255))
        print center
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
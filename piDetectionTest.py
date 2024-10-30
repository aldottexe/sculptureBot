import cv2
from picamera2 import Picamera2

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

picam2 = Picamera2()
picam2.start()

frame = picam2.capture_array()
 
    # Convert to grayscale (face detection works better in grayscale)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) > 0:
    print("found a face!!!")
else:
    print("no faces found.")

# Display the result
cv2.imshow("Face Detection", frame)

# Release resources
cv2.destroyAllWindows()
picam2.stop()

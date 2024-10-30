import torch
import cv2
from picamera2 import Picamera2

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

picam2 = Picamera2()
picam2.start()

try:
    while True: 
        frame = picam2.capture_array()

        # Convert to grayscale (face detection works better in grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Perform detection
        results = model(gray)
    
        # Display the results
        results.render()  # Annotate the frame with detections
        cv2.imshow("YOLOv5 Detection", results.ims[0])
    
        people = [p for p in results.xywhn[0].numpy() if int(p[-1]) == 0 & int(p[-1]) > 0.6]
        
        if len(people) > 0:
            print(f'found someone! ({len(people)})')
        print(people)

except KeyboardInterrupt:
    picam2.stop()

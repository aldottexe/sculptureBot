import torch
import cv2

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Access the video feed
cap = cv2.VideoCapture(0) # Change '0' if using an external camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform detection
    results = model(frame)
    
    # Display the results
    results.render() # Annotate the frame with detections
    cv2.imshow("YOLOv5 Detection", results.ims[0])

    # filters if confidence is above .6 and is person (qualifier is 0)
    people = [p for p in results.xywhn[0].numpy() if (int(p[-1]) == 0) & (float(p[-2]) > .6)]
    print(people)

    # Exit with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

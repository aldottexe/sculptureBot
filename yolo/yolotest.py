import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Run inference on an image or a video
# results = model('../my_image.jpg')
results = model('../toothbrush.jpg')

people = [p for p in results.xywhn[0].numpy() if int(p[-1]) == 0]

print(people)
results.show()  # Display the results

from ultralytics import YOLO

# Load a model

model = YOLO('/home/jrzvnn/Downloads/yolo/detect/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model('/home/jrzvnn/Downloads/yolo/detect/train/manila_cathedral_16.png')  # predict on an image

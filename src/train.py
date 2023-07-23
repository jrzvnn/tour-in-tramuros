from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="/home/jrzvnn/Documents/Projects/tour-in-tramuros/data/data.yml", epochs=1)  # train the model

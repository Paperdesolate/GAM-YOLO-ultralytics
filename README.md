
 #- [-1, 1, GAM, []]

This line of code in AMs-V8  indicates the location of GAM insertion, which can be changed


Install
Pip install the ultralytics package including all requirements in a Python>=3.8 environment with PyTorch>=1.8.

PyPI version Downloads

pip install ultralytics
For alternative installation methods including Conda, Docker, and Git, please refer to the Quickstart Guide.

Usage
CLI
YOLOv8 may be used directly in the Command Line Interface (CLI) with a yolo command:

yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
yolo can be used for a variety of tasks and modes and accepts additional arguments, i.e. imgsz=640. See the YOLOv8 CLI Docs for examples.

Python
YOLOv8 may also be used directly in a Python environment, and accepts the same arguments as in the CLI example above:

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco128.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
See YOLOv8 Python Docs for more examples.

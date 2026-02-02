
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


Segmentation (COCO)
See Segmentation Docs for usage examples with these models trained on COCO-Seg, which include 80 pre-trained classes.

Model	size
(pixels)	mAPbox
50-95	mAPmask
50-95	Speed
CPU ONNX
(ms)	Speed
A100 TensorRT
(ms)	params
(M)	FLOPs
(B)
YOLOv8n-seg	640	36.7	30.5	96.1	1.21	3.4	12.6
YOLOv8s-seg	640	44.6	36.8	155.7	1.47	11.8	42.6
YOLOv8m-seg	640	49.9	40.8	317.0	2.18	27.3	110.2
YOLOv8l-seg	640	52.3	42.6	572.4	2.79	46.0	220.5
YOLOv8x-seg	640	53.4	43.4	712.1	4.02	71.8	344.1
mAPval values are for single-model single-scale on COCO val2017 dataset.
Reproduce by yolo val segment data=coco-seg.yaml device=0
Speed averaged over COCO val images using an Amazon EC2 P4d instance.
Reproduce by yolo val segment data=coco-seg.yaml batch=1 device=0|cpu

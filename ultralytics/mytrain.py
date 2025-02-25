from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('D:/ultralytics/ultralytics/cfg/models/v8/yolov8-seg.yaml')
    model = YOLO('D:/ultralytics/yolov8m-seg.pt')

    model.train(data='D:/ultralytics/ultralytics/cfg/datasets/coco8-seg.yaml')
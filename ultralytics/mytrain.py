from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO(':.yaml')
    model = YOLO('.pt')

    model.train(data='.yaml')

from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/DTH-YOLO.yaml')
    model.train(data='ultralytics/cfg/datasets/mousehole.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=20,
                workers=10,
                device='0',
                optimizer='SGD',
                # resume='True',
                project='runs/train',
                name='1111',
                )


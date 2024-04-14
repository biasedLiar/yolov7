# train model
python train.py --epochs 100 --workers 4 --device 0 --batch-size 32 --data data/pothole.yaml --img 640 640 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml

python train.py --epochs 100 --workers 4 --device 0 --batch-size 32 --data data/pothole.yaml --img 1024 128 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml

# run inference
python detect.py --source ./inference/videos/road.mp4 --weights ./runs/train/yolov7_tiny_pothole_fixed_res5/weights/best.pt --view-img


python detect.py --source ./inference/videos/road.mp4 --weights ./runs/train/yolov7_tiny_pothole_fixed_res6/weights/best.pt --view-img

118
1265
401

1784

06.6 test
70.9 train
22.5 val

1905

125 test
1351 train
429 val
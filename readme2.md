# train model
python train.py --epochs 100 --workers 4 --device 0 --batch-size 32 --data data/pothole.yaml --img 640 640 --cfg cfg/training/yolov7_pothole-tiny.yaml --weights 'yolov7-tiny.pt' --name yolov7_tiny_pothole_fixed_res --hyp data/hyp.scratch.tiny.yaml

# run inference
python detect.py --source ./inference/videos/road.mp4 --weights ./runs/train/yolov7_tiny_pothole_fixed_res5/weights/best.pt --view-img


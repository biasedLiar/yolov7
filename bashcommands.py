

'''
/home/eliaseb/Documents/potholeYOLO/yolov7/new_dataset/images/train
for file in $(cat Documents/potholeYOLO/yolov7/NAPLab-LiDAR/traintestvalsplit/trainImages.txt); do mv "$file" Documents/potholeYOLO/yolov7/new_dataset/images/train; done
'''


locations = ["labels", "images"]

types = ["train", "test", "val"]

f = open("bashcommands.txt", "w")

for loc in locations:
    for t in types:
        type2 = t
        if type2 == "val":
            type2 = "valid"
        print(f'{type2=}')
        if loc == "labels":
            loc2 = "Labels"
        else:
            loc2 = "Images"
        myString = "for file in $(cat Documents/potholeYOLO/yolov7/NAPLab-LiDAR/traintestvalsplit/" + t + loc2 + ".txt); do mv \"$file\" Documents/potholeYOLO/yolov7/new_dataset/" + loc + "/" + type2 + "; done"
        f.write(myString + "\n")

f.close()

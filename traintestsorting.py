import random

numFiles = 1905

nums = [str(i).zfill(6) for i in range(numFiles)]
random.shuffle(nums)


train = 1351
test = 125
val = 429

assert train + test + val == numFiles, "Test+train+val != files being chosen"

index = 0


################################### Images ######################################
abs_path = "Documents/potholeYOLO/yolov7/NAPLab-LiDAR/images/"

f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/trainImages.txt", "w")

for i in nums[:train]:
    f.write(abs_path + "frame_" + i + ".PNG\n")

f.close()

f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/testImages.txt", "w")

for i in nums[train:train+test]:
    f.write(abs_path + "frame_" + i + ".PNG\n")

f.close()

f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/valImages.txt", "w")

for i in nums[train+test:]:
    f.write(abs_path + "frame_" + i + ".PNG\n")

f.close()



##################### Labels ###############################

abs_path2 = "Documents/potholeYOLO/yolov7/NAPLab-LiDAR/labels_yolo_v1.1/"


f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/trainLabels.txt", "w")

for i in nums[:train]:
    f.write(abs_path2 + "frame_" + i + ".txt\n")

f.close()

f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/testLabels.txt", "w")

for i in nums[train:train+test]:
    f.write(abs_path2 + "frame_" + i + ".txt\n")

f.close()

f = open("yolov7/NAPLab-LiDAR/traintestvalsplit/valLabels.txt", "w")

for i in nums[train+test:]:
    f.write(abs_path2 + "frame_" + i + ".txt\n")

f.close()
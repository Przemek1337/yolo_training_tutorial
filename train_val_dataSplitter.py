import os
import shutil
import random

img_dir = r'/home/szewczyk/Desktop/Yolo/out_img'
label_dir = r'/home/szewczyk/Desktop/Yolo/labels'

train_img_dir = r'/home/szewczyk/Desktop/images/train'
val_img_dir = r'/home/szewczyk/Desktop/images/val'

train_label_dir = r'/home/szewczyk/Desktop/labels/train'
val_label_dir = r'/home/szewczyk/Desktop/labels/val'

# Creating output dir's
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# List of all labels and images
images = os.listdir(img_dir)
random.shuffle(images)

# 80% training section - 20% validation
split_ratio = 0.8
split_index = int(len(images) * split_ratio)

# Splitting into training and validation sections
train_images = images[:split_index]
val_images = images[split_index:]

#
for img in train_images:
    img_path = os.path.join(img_dir, img)
    label_path = os.path.join(label_dir, os.path.splitext(img)[0] + '.txt')
    shutil.copy(img_path, os.path.join(train_img_dir, img))
    shutil.copy(label_path, os.path.join(train_label_dir, os.path.basename(label_path)))

for img in val_images:
    img_path = os.path.join(img_dir, img)
    label_path = os.path.join(label_dir, os.path.splitext(img)[0] + '.txt')
    shutil.copy(img_path, os.path.join(val_img_dir, img))
    shutil.copy(label_path, os.path.join(val_label_dir, os.path.basename(label_path)))

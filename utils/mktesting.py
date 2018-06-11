import numpy as np
import h5py
import cv2
import os
import random

pick_positive = True

test_file = ""
test_label = "unknown"
sub_dir = ""
label_num = 0

if pick_positive:
    label_num = 1
    test_label = "showing symptoms"
    sub_dir = "training\\symptoms\\"
    positive_listing = os.listdir(sub_dir)
    file_list = []
    for file in positive_listing:
        if file.endswith(".jpeg"):
            file_list.append(file)
    test_file = file_list[random.randint(0, len(file_list))]
    
else:
    label_num = 0
    test_label = "not showing symptoms"
    sub_dir = "training\\nosymptoms\\"
    negative_listing = os.listdir(sub_dir)
    file_list = []
    for file in negative_listing:
        if file.endswith(".jpeg"):
            file_list.append(file)
    test_file = file_list[random.randint(0, len(file_list))]

print("Creating test HDF5 file using \"" + test_file + "\" (" + test_label + ")...")

f = h5py.File('img_left_test.hdf5', mode = 'w')
image_shape = (1, 3, 150, 150)
label_shape = (1, 1, 1, 1)

rgb_left_ds = f.create_dataset('RGB_left', image_shape, np.float)
label_ds = f.create_dataset('label', label_shape, np.int32)

img = cv2.imread(sub_dir + test_file)
img = np.rollaxis(img, 2)
rgb_left_ds[0, ...] = img[None]
label_ds[0, 0, 0, 0] = label_num
f.close()

import numpy as np
import h5py
import cv2
import os

positive_count = 0
positive_listing = os.listdir("training\\symptoms\\")
for file in positive_listing:
    if file.endswith(".jpeg"):
        positive_count += 1

negative_count = 0
negative_listing = os.listdir("training\\nosymptoms\\")
for file in negative_listing:
    if file.endswith(".jpeg"):
        negative_count += 1

print("Positive count = " + str(positive_count))
print("Negative count = " + str(negative_count))

print("Creating HDF5 File...")

f = h5py.File('img_left_train.hdf5', mode = 'w')
image_shape = (positive_count + negative_count, 3, 150, 150)
label_shape = (positive_count + negative_count, 1, 1, 1)

rgb_left_ds = f.create_dataset('RGB_left', image_shape, np.float)
label_ds = f.create_dataset('label', label_shape, np.int32)

i = 0

for file in positive_listing:
    if file.endswith(".jpeg"):
        fn = "training\\symptoms\\" + file
        img = cv2.imread(fn)
        img = np.rollaxis(img, 2)
        rgb_left_ds[i, ...] = img[None]
        label_ds[i, 0, 0, 0] = 1
        i += 1

for file in negative_listing:
    if file.endswith(".jpeg"):
        fn = "training\\nosymptoms\\" + file
        img = cv2.imread(fn)
        img = np.rollaxis(img, 2)
        rgb_left_ds[i, ...] = img[None]
        label_ds[i, 0, 0, 0] = 0
        i += 1

f.close()

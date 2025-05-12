import numpy as np
import os
import cv2
import scipy.ndimage

from variables import px, filepath, darkframe_filepath

#Load in the locally saved experimental data:
def load_experimental_data(path):
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        if img is not None:
            images.append(img)
    return images

#Image data preprocessing (consistent re-size, greyscale, normalisation):
def preprocess(pixelLength, gallery):
    imgs = []
    for i in gallery:
        resize = cv2.resize(i, (pixelLength,pixelLength))
        grey = cv2.cvtColor(resize, cv2.COLOR_RGB2GRAY) #convert to greyscale
        normalise = grey/np.max(grey) #also could use tf implementation, shouldnt matter tho
        imgs.append(normalise)
    img_stack = np.stack(imgs, axis=-1) #stack images, shape of input will be (128,128,20)
    NN_data = np.expand_dims(img_stack, axis=0) #add batch dimension, use as input to CNN
    return imgs, NN_data

#Rotating images and heightmaps, to augment more training data:
def augment_data(images, labels, angles):
    augmented_images = []
    augmented_labels = []
    for angle in angles:
        for img, label in zip(images, labels):
            # Rotate the image
            rotated_img = scipy.ndimage.rotate(img, angle, reshape=False)
            # Rotate the corresponding heightmap
            rotated_lbl = scipy.ndimage.rotate(label, angle, reshape=False)
            
            augmented_images.append(rotated_img)
            augmented_labels.append(rotated_lbl)
    
    # Convert to numpy arrays
    augmented_images = np.array(augmented_images)
    augmented_labels = np.array(augmented_labels)
    
    return augmented_images, augmented_labels


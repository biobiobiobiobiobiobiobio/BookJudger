import keras
from keras.models import load_model
import sys
import cv2
import numpy as np

x_test = np.zeros((0,4608))
model = load_model("test1.h5")
im = cv2.imread(r"..\..\books\\" + sys.argv[1] + ".png")
im = cv2.resize(im, (32, 48))
im = np.divide(im, 255)
im = im.flatten()
x_test = np.concatenate([x_test, im[None,:]])
print(model.predict(x_test))
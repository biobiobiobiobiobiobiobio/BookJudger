import keras
from keras.models import load_model
import sys
import cv2
import numpy as np

x_test = np.zeros((0,4608))
model = load_model("model102.h5")
im = cv2.imread(sys.argv[1])
im = cv2.resize(im, (32, 48))
im = np.divide(im, 255)
im = im.flatten()
x_test = np.concatenate([x_test, im[None,:]])
f = open("output.txt", "a")
print(float(model.predict(x_test)), file=f)
f.close()
import keras
from keras.models import load_model
import sys
import cv2
import numpy as np

x_test = np.zeros((0,4608))
model = load_model(r"D:\Code\Hackathons\BookJudger\NeuralNet\hdmodel.h5")
im = cv2.imread(sys.argv[1])
im = cv2.resize(im, (32, 48))
im = np.divide(im, 255)
im = im.flatten()
x_test = np.concatenate([x_test, im[None,:]])
f = open(r"D:\Code\Hackathons\BookJudger\Cam_to_book\data\hdoutput.txt", "w")
print(float(model.predict(x_test)))
f.write(str(float(model.predict(x_test))))
f.close()
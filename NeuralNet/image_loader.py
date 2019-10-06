import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, RMSprop
from continuous_data_network import *
import numpy as np
import cv2

# Generate dummy data
#im1 = cv2.imread("1.jpg")
#im1 = np.divide(im1, 255)
#im1 = im1.flatten()
#im2 = cv2.imread("2.jpg")
#im2 = np.divide(im2, 255)
#im2 = im2.flatten()
#im3 = cv2.imread("3.jpg")
#im3 = np.divide(im3, 255)
#im3 = im3.flatten()

index = 1
indexer = open(r"..\..\books\index.txt")
x_test = np.zeros((0,4608))
y_test = np.array([])
line = indexer.readline()
while index < 440:
	im = cv2.imread(r"..\..\books\\" + str(index) + ".jpg")
	im = cv2.resize(im, (32, 48))
	im = np.divide(im, 255)
	im = im.flatten()
	x_test = np.concatenate([x_test, im[None,:]])
	y_test = np.append(y_test, float(line))
	index += 1
	line = indexer.readline()
x_train = np.zeros((0,4608))
y_train = np.array([])

while index < 4699:
	im = cv2.imread(r"..\..\books\\" + str(index) + ".jpg")
	im = cv2.resize(im, (32, 48))
	im = np.divide(im, 255)
	im = im.flatten()
	x_train = np.concatenate([x_train, im[None,:]])
	y_train = np.append(y_train, float(line))
	index += 1
	line = indexer.readline()

#modelType1 = []
#for n in range(0, 10):	
model = train_continuous_network(x_train, y_train)
#	modelType1.append(model)
#modelType2 = []
#for n in range(0, 5):	
#	model = train_continuous_network2(x_train, y_train)
#	modelType2.append(model)
#modelType3 = []
#for n in range(0, 5):	
#	model = train_continuous_network3(x_train, y_train)
#	modelType3.append(model)
#modelType4 = []
#for n in range(0, 5):	
#	model = train_continuous_network4(x_train, y_train)
#	modelType4.append(model)
#for i in range(0, 10):
#	print()
#	print("Base Model " + str(i))
#	test_model(x_test, y_test, modelType1[i])
save_model(model, "hdmodel")
#for i in range(0, 5):
#	print()
#	print("Model 2" + str(i))
#	test_model(x_test, y_test, modelType2[i])
#	save_model(model, "model20" + str(i))
#for i in range(0, 5):
#	print()
#	print("Model 3 " + str(i))
#	test_model(x_test, y_test, modelType3[i])
#	save_model(model, "model30" + str(i))
#for i in range(0, 5):
#	print()
#	print("Model 4 " + str(i))
#	test_model(x_test, y_test, modelType4[i])
#	save_model(model, "model30" + str(i))
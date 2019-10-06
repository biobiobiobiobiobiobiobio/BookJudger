import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, RMSprop
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
indexer = open(r"..\..\books\index.txt") #finish
x_test = np.zeros((0,11250))
y_test = np.array([])
line = indexer.readline()
while index < 20:
	im = cv2.imread(r"..\..\books\\" + str(index) + ".png")
	im = np.divide(im, 255)
	im = im.flatten()
	x_test = np.concatenate([x_test, im[None,:]])
	y_test = np.append(y_test, line)
	index += 1
	line = indexer.readline()
x_train = np.zeros((0,11250))
y_train = np.array([])

while index < 105:
	im = cv2.imread(r"..\..\books\\" + str(index) + ".png")
	im = np.divide(im, 255)
	im = im.flatten()
	x_train = np.concatenate([x_train, im[None,:]])
	y_train = np.append(y_train, line)
	index += 1
	line = indexer.readline()

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=11250))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='relu'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
rms = RMSprop(lr=0.01)
model.compile(loss='mean_squared_error',
              optimizer=rms,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)

score = model.evaluate(x_test, y_test, batch_size=128)
model.save("test1.h5")
print(score)

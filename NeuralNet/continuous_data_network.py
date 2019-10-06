import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, RMSprop
import numpy as np
import cv2

def train_continuous_network(x_train, y_train):
	model = Sequential()
	# Dense(64) is a fully-connected layer with 64 hidden units.
	# in the first layer, you must specify the expected input data shape:
	# here, 20-dimensional vectors.
	model.add(Dense(100, activation='sigmoid', input_dim=4608))
	#model.add(Dropout(0.1))
	model.add(Dense(20, activation='relu'))
	#model.add(Dropout(0.1))
	model.add(Dense(1, activation='linear'))
	sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
	rms = RMSprop(lr=0.01)
	model.compile(loss='mean_squared_error',
		optimizer=sgd)
	
	model.fit(x_train, y_train,
		epochs=1000,
		batch_size=128)

	return model
	
def train_continuous_network2(x_train, y_train):
	model = Sequential()
	# Dense(64) is a fully-connected layer with 64 hidden units.
	# in the first layer, you must specify the expected input data shape:
	# here, 20-dimensional vectors.
	model.add(Dense(200, activation='sigmoid', input_dim=4608))
	#model.add(Dropout(0.1))
	model.add(Dense(100, activation='relu'))
	#model.add(Dropout(0.1))
	model.add(Dense(1, activation='relu'))
	sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
	rms = RMSprop(lr=0.01)
	model.compile(loss='mean_squared_error',
		optimizer=sgd)
	
	model.fit(x_train, y_train,
		epochs=200,
		batch_size=128)

	return model
	
def train_continuous_network3(x_train, y_train):
	model = Sequential()
	# Dense(64) is a fully-connected layer with 64 hidden units.
	# in the first layer, you must specify the expected input data shape:
	# here, 20-dimensional vectors.
	model.add(Dense(100, activation='sigmoid', input_dim=4608))
	model.add(Dropout(0.1))
	model.add(Dense(20, activation='relu'))
	model.add(Dropout(0.1))
	model.add(Dense(1, activation='linear'))
	sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
	rms = RMSprop(lr=0.01)
	model.compile(loss='mean_squared_error',
		optimizer=sgd)
	
	model.fit(x_train, y_train,
		epochs=200,
		batch_size=128)

	return model
	
def train_continuous_network4(x_train, y_train):
	model = Sequential()
	# Dense(64) is a fully-connected layer with 64 hidden units.
	# in the first layer, you must specify the expected input data shape:
	# here, 20-dimensional vectors.
	model.add(Dense(200, activation='sigmoid', input_dim=4608))
	#model.add(Dropout(0.1))
	model.add(Dense(100, activation='relu'))
	#model.add(Dropout(0.1))
	model.add(Dense(20, activation='relu'))
	#model.add(Dropout(0.1))
	model.add(Dense(1, activation='relu'))
	sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
	rms = RMSprop(lr=0.01)
	model.compile(loss='mean_squared_error',
		optimizer=sgd)
	
	model.fit(x_train, y_train,
		epochs=200,
		batch_size=128)

	return model

def save_model(model, name):
	model.save(name + ".h5")

def test_model(x_test, y_test, model):
	score = model.evaluate(x_test, y_test, batch_size=128)
	print(score)
	predict = model.predict(x_test)
	predict = predict.flatten()
	varience = np.var(predict)
	print("Varience:" + str(varience))
	print("Normal:" + str(np.sqrt(varience)))
	
def laod_model(path):
	model = load_model("model.h5")

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, RMSprop

# Generate dummy data
import numpy as np
x_train = np.random.random((1000, 4608))
y_train = np.random.normal(loc=10, scale=5, size=(1000, 1))
x_test = np.random.random((100, 4608))
y_test = np.random.normal(loc=10, scale=5, size=(100, 1))

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=4608))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='relu'))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
rms = RMSprop(lr=0.01)
model.compile(loss='mean_squared_error',
              optimizer=rms,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=100,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

rand = np.random.random((10, 4608))
model.predict(rand)
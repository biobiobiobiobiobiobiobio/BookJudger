import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD, RMSprop

model2 = load_model("test.h5")

rand = np.random.random((10, 4608))
model2.predict(rand)
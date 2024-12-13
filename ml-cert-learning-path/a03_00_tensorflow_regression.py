import tensorflow as tf
import keras
from keras.src.utils import plot_model
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# Input layer shape - Same shape as number of features (e.g. 3 for # bedrooms, # bathrooms, # car spaces in housing price prediction)
# Hidden layer(s) - Problem specific, minimum = 1, maximum = unlimited
# Neurons per hidden layer - Problem specific, generally 10 to 100
# Output layer shape - Same shape as desired prediction shape (e.g. 1 for house price)
# Hidden activation - Usually ReLU (rectified linear unit)
# Output activation - None, ReLU, logistic/tanh
# Loss function - MSE (mean square error) or MAE (mean absolute error)/Huber (combination of MAE/MSE) if outliers
# Optimizer - SGD (stochastic gradient descent), Adam

X = np.array([-7.0, -4.0, -1.0, 2.0, 5.0, 8.0, 11.0, 14.0])
y = np.array([3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])

plt.scatter(X, y)
plt.savefig("fig.png")

house_info = tf.constant(["bedroon", "bathroom", "garage"])
house_price = tf.constant([939700])

input_shape = X.shape
output_shape = y.shape

## turn to numpy
X = tf.constant(X)
y = tf.constant(y)

## steps in modelling with tensorflow
tf.random.set_seed(42)

####### FIRST MODEL
## 1. creating a model - define the input and output layers, as well as the hidden layers for a deep learning model
model = keras.Sequential([keras.layers.Dense(1)])

# model = keras.Sequential()
# model.add(keras.layers.Dense(1))

## 2. Compiling a model - define the loss function (in other words, the function which tells how wrong our model how wrong is)
##                        and evaluation metrics (what we can use to interprete the performance of our model)
model.compile(
    optimizer=keras.optimizers.SGD(),  # stochastic gradient descent
    loss=keras.losses.MeanAbsoluteError(),  # mean absolute error
    metrics=[keras.metrics.MeanAbsoluteError()],
)

## 3. Fitting a model - letting the model try to find patterns between X & y
model.fit(tf.expand_dims(X, axis=-1), y, epochs=5)

## 4. Evaluate the model
# model.evaluate(...)

## Prediction
model.predict(np.array([17.0]))

####### SECOND MODEL
tf.random.set_seed(42)

model = keras.Sequential(
    [
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(1),
    ]
)

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.MeanAbsoluteError(),
    metrics=[keras.metrics.MeanAbsoluteError()],
)

model.fit(tf.expand_dims(X, axis=-1), y, epochs=100)

model.predict(np.array([17.0]))

####### THIRD MODEL
tf.random.set_seed(42)

model = keras.Sequential(
    [
        keras.layers.Dense(100, activation="relu"),
        keras.layers.Dense(1),
    ]
)

model.compile(
    optimizer=keras.optimizers.SGD(),
    loss=keras.losses.MeanAbsoluteError(),
    metrics=[keras.metrics.MeanAbsoluteError()],
)

model.fit(tf.expand_dims(X, axis=-1), y, epochs=100)

model.predict(np.array([17.0]))

## ways to improve a deep model
# adding layers
# increase the number of hidden units
# change the activation functions
# change the optimisation function
# change the learning rate (important)
# fitting on more data
# fitting for longer (higher epochs)

##### EVALUATION
X = tf.range(-100, 100, 4)
y = X + 10

## visualise data
plt.scatter(X, y)
plt.savefig("fig.png")

## 3 sets
## training set - 70 to 80%
## validation set - 10 to 15%
## test set - 10 to 15%

X_train, X_test = X[:40], X[40:]
y_train, y_test = y[:40], y[40:]

plt.scatter(X_train, y_train, c="b", label="Training data")
plt.scatter(X_test, y_test, c="g", label="Testing data")
plt.legend()
plt.savefig("fig.png")

model = keras.Sequential([keras.layers.Dense(1, input_shape=[1])])
model.compile(
    optimizer=keras.optimizers.SGD(),
    loss=keras.losses.MeanAbsoluteError(),
    metrics=[keras.metrics.MeanAbsoluteError()],
)
model.summary()

plot_model(model=model)

model.fit(tf.expand_dims(X_train, axis=-1), y_train, epochs=100, verbose=0)

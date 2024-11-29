import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf

#### initialization of tensors
x = tf.constant(4, shape=(1, 1), dtype=tf.float32)
print(x)
x = tf.constant([[1, 2, 3], [4, 5, 6]])
print(x)
x = tf.ones((3, 3))
print(x)
x = tf.zeros((2, 3))
print(x)
x = tf.eye(3)
print(x)
x = tf.random.normal((3, 3), mean=0, stddev=1)
print(x)
x = tf.random.uniform((1, 3), minval=0, maxval=1)
print(x)
x = tf.range(start=1, limit=10, delta=2)
print(x)
x = tf.cast(x, dtype=tf.float64)
print(x)

#### mathematical operations
## element-wise
x = tf.constant([1, 2, 3])
y = tf.constant([9, 8, 7])
print(tf.add(x, y))
print(x + y)
print(tf.subtract(x, y))
print(x - y)
print(tf.divide(x, y))
print(x / y)
print(tf.multiply(x, y))
print(x * y)
print(tf.tensordot(x, y, axes=1))
print(tf.reduce_sum(x * y, axis=0))
print(x**5)

## matrix
x = tf.random.normal((2, 3))
y = tf.random.normal((3, 4))
print(tf.matmul(x, y))
print(x @ y)

#### indexing
x = tf.constant([0, 1, 1, 2, 3, 1, 2, 3])
print(x[:])
print(x[1:])
print(x[1:3])
print(x[::2])
print(x[::-1])
print(tf.gather(x, [0, 1]))

x = tf.constant([[1, 2], [3, 4], [5, 6]])
print(x[0, :])
print(x[0:2, :])

#### reshaping
x = tf.range(9)
x = tf.reshape(x, (3, 3))
print(x)
x = tf.transpose(x, perm=[1, 0])
print(x)

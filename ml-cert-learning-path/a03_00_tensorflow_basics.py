import tensorflow as tf
import numpy as np

print(tf.__version__)

#### Introduction to tensors

## tf.constant
scala = tf.constant(7)
scala.ndim

vector = tf.constant([10, 10])
vector.ndim

matrix = tf.constant([[10, 7], [7, 10]])
matrix.ndim

another_matrix = tf.constant(
    [[10.0, 7.0], [3.0, 2.0], [8.0, 9.0]],
    dtype=tf.float16,
)
another_matrix.ndim

tensor = tf.constant(
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
        ]
    ]
)
tensor.ndim

# scala - a single number
# vector - a number with direction (eg wind speed and direction)
# matrix - a 2-dimensional array of numbers
# tensor - an n-dimensional array of numbers, n can be any number

x1 = tf.constant([2, 3, 4])  # (3,)
x2 = tf.stack([x1, x1])  # (2, 3)
x3 = tf.stack([x2, x2, x2, x2])  # (4, 2, 3)
x4 = tf.stack([x3, x3])  # (2, 4, 2, 3)

## tf.Variable
changeable_tensor = tf.Variable([10, 7])
unchangeable_tensor = tf.constant([10, 7])

changeable_tensor[0].assign(7)
changeable_tensor[0].assign_add(7)
changeable_tensor[0].assign_sub(7)
# unchangeable_tensor[0].assign(7) # error

## Creating random tensors
random_1 = tf.random.Generator.from_seed(42)
random_1 = random_1.normal(shape=(3, 2))
random_2 = tf.random.Generator.from_seed(42)
random_2 = random_2.normal(shape=(3, 2))
random_1 == random_2

## Shuffle the order of elements in a tensor
not_shuffled = tf.constant(
    [
        [10, 7],
        [3, 4],
        [2, 5],
    ]
)

tf.random.set_seed(42)
tf.random.shuffle(not_shuffled, seed=42)

## Other ways to make tensors
tf.ones([10, 7])
tf.zeros(shape=(3, 4))

numpy_A = np.arange(1, 25, dtype=np.int32)
A = tf.constant(numpy_A, shape=(2, 3, 4))
B = tf.constant(numpy_A)

#### Getting information from tensors
# shape - length of each of the dimensions of a tensor (tensor.shape)
# rank - number of dimensions (tensor.ndim)
# axis or dimension - particular dimension (tensor[0], tensor[:, 1]...)
# size - total number of items (tf.size(tensor))

rank_4_tensor = tf.zeros(shape=(2, 3, 4, 5))
rank_4_tensor[0]
rank_4_tensor[0][0]
rank_4_tensor.shape
rank_4_tensor.dtype
rank_4_tensor.ndim
tf.size(rank_4_tensor).numpy()

## indexing tensors
rank_4_tensor[:2, :2, :2, :2]
rank_4_tensor[:1, :1, :1, :]
rank_4_tensor[:1, :1, :, :1]

rank_2_tensor = tf.constant([[10, 7], [3, 4]])
rank_2_tensor[:, :-1]

rank_2_tensor[..., tf.newaxis]
rank_2_tensor[:, :, tf.newaxis]
tf.expand_dims(rank_2_tensor, axis=-1)  # -1 means expand the final axis
tf.expand_dims(rank_2_tensor, axis=0)

#### Manipulating tensors

## element-wise operations
tensor = tf.constant([[10, 7], [3, 4]])
tensor + 10
tensor * 10
tf.multiply(tensor, 10)

## matrix multiplication
tensor = tf.constant([[10, 7], [3, 4]])
tf.matmul(tensor, tensor)

tensor * tensor  # element-wise
tensor @ tensor  # matrix multiplication

X = tf.constant([[1, 2], [3, 4], [5, 6]])
Y = tf.constant([[7, 8], [9, 10], [11, 12]])

# tf.matmul(X, Y) # error
tf.matmul(X, Y, transpose_a=True)
tf.matmul(tf.transpose(X), Y)
tf.matmul(X, Y, transpose_b=True)
tf.matmul(tf.reshape(X, shape=(2, 3)), Y)
tf.matmul(X, tf.reshape(Y, shape=(2, 3)))

## dot product
# tf.matmul() or tf.tensordot()
tf.tensordot(tf.transpose(X), Y, axes=1)

## change data types
B = tf.constant([1.7, 7.4])
# tf.constant([7, 10])
tf.cast(B, dtype=tf.float16)
tf.cast(tf.constant([7.0, 10.1]), dtype=tf.int32)

## aggregation
D = tf.constant([-7, -10])
tf.abs(D)

np_array = np.random.randint(0, 100, size=50)
E = tf.constant(np_array)
tf.math.reduce_min(E)
tf.math.reduce_max(E)
tf.math.reduce_mean(E)
tf.math.reduce_sum(E)
tf.math.reduce_variance(tf.cast(E, dtype=tf.float32))
tf.math.reduce_std(tf.cast(E, dtype=tf.float32))

var = tf.math.reduce_sum(
    tf.math.square(
        tf.cast(E, dtype=tf.float32) - tf.math.reduce_mean(tf.cast(E, dtype=tf.float32))
    )
) / int(tf.size(E).numpy())
std = tf.math.sqrt(var)

## positional min/max
F = tf.random.uniform(shape=(50,))

tf.math.argmax(F)
F[tf.math.argmax(F)]
tf.math.reduce_max(F)

tf.math.argmin(F)

## squeezing a tensor (removing all single dimensions)
G = tf.constant(tf.random.uniform(shape=(50,)), shape=(1, 1, 1, 1, 50))
G_squeezed = tf.squeeze(G)

## one hot encoding
some_list = [0, 1, 3, 2]  # red, green, blue, purple
tf.one_hot(some_list, depth=4)
tf.one_hot(some_list, depth=4, on_value="on", off_value="off")

## more
H = tf.range(0, 10)
tf.math.square(H)
tf.math.sqrt(tf.cast(H, dtype=tf.float32))
tf.math.log(tf.cast(H, dtype=tf.float32))

#### Tensors & NumPy
J = tf.constant(np.array([3.0, 7.0, 10.0]))
np.array(J)
J.numpy()

#### Using @tf.function (a way to speed up your regular Python functions)


#### Using GPUs with TensorFlow (or TPUs)

## finding access to GPUs
tf.config.list_physical_devices()
tf.config.list_physical_devices("CPU")
tf.config.list_physical_devices("GPU")

# !nvidia-smi

#### Exercises

# Create a vector, scalar, matrix and tensor with values of your choosing using tf.constant().
# Find the shape, rank and size of the tensors you created in 1.
# Create two tensors containing random values between 0 and 1 with shape [5, 300].
# Multiply the two tensors you created in 3 using matrix multiplication.
# Multiply the two tensors you created in 3 using dot product.
# Create a tensor with random values between 0 and 1 with shape [224, 224, 3].
# Find the min and max values of the tensor you created in 6 along the first axis.
# Created a tensor with random values of shape [1, 224, 224, 3] then squeeze it to change the shape to [224, 224, 3].
# Create a tensor with shape [10] using your own choice of values, then find the index which has the maximum value.
# One-hot encode the tensor you created in 9.

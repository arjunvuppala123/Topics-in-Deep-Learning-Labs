#imports all needed libraries
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt

#creating an array of input
input = np.linspace(-5, 5, 15)

"""Implementation of sigmoid function using tensorflow"""

#prints the output in form of array
output = tf.nn.sigmoid(input, name ='sigmoid')

sess = tf.compat.v1.Session()
plt.plot(input, sess.run(output),marker = "o")
plt.title("implementation of sigmoid function with tensorflow")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()



"""Implementation of tanh"""

output_tanh = tf.nn.tanh(input, name ='tanh')

sess = tf.compat.v1.Session()
plt.plot(input, sess.run(output_tanh),marker = "o")
plt.title("implementation of tanh function with tensorflow")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()



"""Derivative of sigmoid"""

def sigmoid_derivative(x):
  s = 1/(1+np.exp(-x))
  ds = s*(1-s)
  return s,ds
output,derivative = sigmoid_derivative(input)

print(output)

print(type(derivative))

sess = tf.compat.v1.Session()
plt.plot(input, sess.run(tf.convert_to_tensor(output)),marker = "o")
plt.plot(input, sess.run(tf.convert_to_tensor(derivative)),marker = "o")
plt.title("implementation of sigmoid function with tensorflow")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()



"""Derivative of Tanh"""

def tanh_derivative(x):
  t = ((np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)))
  dt = 1-t**2
  return t,dt
output,derivative = tanh_derivative(input)

sess = tf.compat.v1.Session()
plt.plot(input, sess.run(tf.convert_to_tensor(output)),marker = "o")
plt.plot(input, sess.run(tf.convert_to_tensor(derivative)),marker = "o")
plt.title("implementation of tanh function with tensorflow")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()


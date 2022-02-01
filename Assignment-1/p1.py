import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def xor(a,b):
  return ((a&~b)|(~a&b))
a=tf.constant([False,False,True,True])
b=tf.constant([False,True,False,True])

sess = tf.compat.v1.Session()
print("Input is a = ",sess.run(a) ," b = ", sess.run(b))
print("output is =", sess.run(xor(a,b)))


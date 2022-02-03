import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

input1 = tf.constant(3)
input2 = tf.constant(4)

e1 = tf.add(input1 , input2)
e2 = tf.add(input2 , 1)

res = tf.multiply(e1,e2)

sess = tf.compat.v1.Session()
writer = tf.summary.FileWriter("./logs",sess.graph)
print(sess.run(res))




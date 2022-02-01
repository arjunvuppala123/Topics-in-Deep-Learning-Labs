import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

tf.version.VERSION

a = int(input("Enter the first value = "))
b = int(input("Enter the  second value = "))

x = tf.constant(a)
y = tf.constant(b)

output = (x+y)*(y+1)

sess = tf.compat.v1.Session()
print(sess.run(output))




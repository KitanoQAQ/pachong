import tensorflow as tf

a = tf.constant([1,2,3,4,5])

var = tf.Variable(tf.random_normal([2,3],mean=0.0,stddev=1.0),name='variable')

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run([a,var]))
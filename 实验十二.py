import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0,name='a')
b = tf.constant(1.0,name='b')
c = tf.add(a,b,name='add')
with tf.Session() as sess:
    fw = tf.summary.FileWriter('./summary',graph=sess.graph)
    print(sess.run(c))
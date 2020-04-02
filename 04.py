



import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a,b)

graph = tf.get_default_graph()
print(graph)

graph2 = tf.Graph()
print(graph2)
with graph2.as_default():
    d = tf.constant(11.0)

with tf.Session(graph=graph2) as sess:
    print(sess.run(d))
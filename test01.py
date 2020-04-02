import tensorflow as tf

hello = tf.constant('hello,world')
print(hello)

a = tf.constant(5.0)
b = tf.constant(1.0)
c = tf.add(a,b)
print(c)

graph = tf.get_default_graph()
print(graph)

with tf.Session() as sess:
    print(sess.run(c))
    print(a.graph)
    print(c.graph)
    print(sess.graph)



















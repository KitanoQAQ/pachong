import tensorflow as tf

pld = tf.placeholder(tf.float32,[None,3])
print(pld)

pld.set_shape([4,3])
print(pld)

new_pld = tf.reshape(pld,[3,4])
print(new_pld)

with tf.Session() as sess:
    pass
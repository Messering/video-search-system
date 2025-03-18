import tensorflow as tf

class PixelDiffLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(PixelDiffLayer, self).__init__(**kwargs)

    def call(self, inputs):
        frame1, frame2 = inputs
        diff = tf.abs(frame1 - frame2)
        diff_mean = tf.reduce_mean(diff, axis=[1, 2, 3], keepdims=True)
        return diff_mean

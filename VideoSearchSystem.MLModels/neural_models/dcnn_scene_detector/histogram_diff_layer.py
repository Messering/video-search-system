import tensorflow as tf

class HistogramDiffLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(HistogramDiffLayer, self).__init__(**kwargs)

    def call(self, inputs):
        frame1, frame2 = inputs
        diff = tf.math.squared_difference(frame1, frame2)
        diff_sum = tf.reduce_sum(diff, axis=[1, 2, 3], keepdims=True)
        return diff_sum

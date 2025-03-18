from tensorflow.keras.layers import MaxPooling2D, GlobalAveragePooling2D

def max_pooling_block(x, pool_size=(2, 2), strides=(2, 2)):
    return MaxPooling2D(pool_size=pool_size, strides=strides)(x)

def global_avg_pooling_block(x):
    return GlobalAveragePooling2D()(x)

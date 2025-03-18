from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation

def conv_block(x, filters, kernel_size=(3, 3), activation='relu', padding='same'):
    x = Conv2D(filters, kernel_size, padding=padding)(x)
    x = BatchNormalization()(x)
    x = Activation(activation)(x)
    return x

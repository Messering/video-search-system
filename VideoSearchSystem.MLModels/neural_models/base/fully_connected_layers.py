from tensorflow.keras.layers import Dense, Dropout

def fc_block(x, units, activation='relu', dropout_rate=0.5):
    x = Dense(units, activation=activation)(x)
    x = Dropout(dropout_rate)(x)
    return x

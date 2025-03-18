import tensorflow as tf

def create_fnn_optimizer(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')  # 3 параметри α, β, γ
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

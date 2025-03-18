from tensorflow.keras.layers import Input, concatenate
from tensorflow.keras.models import Model
from neural_models.base.convolutional_layers import conv_block
from neural_models.base.pooling_layers import max_pooling_block, global_avg_pooling_block
from neural_models.base.fully_connected_layers import fc_block
from neural_models.dcnn_scene_detector.histogram_diff_layer import HistogramDiffLayer
from neural_models.dcnn_scene_detector.pixel_diff_layer import PixelDiffLayer

def create_scene_detector(input_shape=(224, 224, 3)):
    frame1_input = Input(shape=input_shape)
    frame2_input = Input(shape=input_shape)

    # Shared CNN-branch
    def cnn_branch(frame_input):
        x = conv_block(frame_input, 32)
        x = max_pooling_block(x)
        x = conv_block(x, 64)
        x = global_avg_pooling_block(x)
        return x

    frame1_features = cnn_branch(frame1_input)
    frame2_features = cnn_branch(frame2_input)

    # Обчислюємо гістограмні і піксельні різниці
    hist_diff = HistogramDiffLayer()([frame1_input, frame2_input])
    pix_diff = PixelDiffLayer()([frame1_input, frame2_input])

    combined_features = concatenate([frame1_features, frame2_features, hist_diff, pix_diff])

    x = fc_block(combined_features, 128)
    output = Dense(2, activation='softmax')(x)  # 2 класи: hard cut, soft cut

    model = Model(inputs=[frame1_input, frame2_input], outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model

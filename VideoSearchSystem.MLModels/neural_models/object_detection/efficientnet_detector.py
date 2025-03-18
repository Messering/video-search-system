import tensorflow as tf
from efficientnet.tfkeras import EfficientNetB0, preprocess_input
import numpy as np

class EfficientNetDetector:
    def __init__(self):
        self.model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')
        self.input_shape = (224, 224)

    def preprocess_frame(self, frame):
        frame_resized = tf.image.resize(frame, self.input_shape)
        frame_array = np.expand_dims(frame_resized.numpy(), axis=0)
        preprocessed_frame = preprocess_input(frame_array)
        return preprocessed_frame

    def extract_features(self, frame):
        preprocessed_frame = self.preprocess_frame(frame)
        features = self.model(preprocessed_frame)
        return features.numpy().flatten()

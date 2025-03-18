import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

class MobileNetDetector:
    def __init__(self, model_url='https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4'):
        self.model = hub.load(model_url)
        self.input_shape = (224, 224)

    def preprocess_frame(self, frame):
        frame_resized = tf.image.resize(frame, self.input_shape) / 255.0
        frame_expanded = tf.expand_dims(frame_resized, axis=0)
        return frame_expanded

    def extract_features(self, frame):
        preprocessed_frame = self.preprocess_frame(frame)
        features = self.model(preprocessed_frame)
        return features.numpy()

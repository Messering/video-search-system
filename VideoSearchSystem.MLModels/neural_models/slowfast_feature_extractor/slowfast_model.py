import tensorflow as tf
import tensorflow_hub as hub

class SlowFastExtractor:
    def __init__(self, model_url='https://tfhub.dev/deepmind/i3d-kinetics-400/1'):
        self.model = hub.load(model_url)

    def extract_features(self, video_clip):
        # очікує тензор форми [batch_size, frames, height, width, channels]
        features = self.model(video=video_clip)
        return features.numpy()

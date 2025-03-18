import numpy as np
from neural_models.object_detection.mobilenet_detector import MobileNetDetector
from neural_models.object_detection.efficientnet_detector import EfficientNetDetector

class ObjectFeaturesExtractor:
    def __init__(self):
        self.mobile_net_detector = MobileNetDetector()
        self.efficient_net_detector = EfficientNetDetector()

    def extract_features(self, frame):
        mobile_features = self.mobile_net_detector.extract_features(frame)
        efficientnet_features = self.efficient_net_detector.extract_features(frame)
        combined_features = np.concatenate([mobile_features.flatten(), efficientnet_features.flatten()])
        return combined_features

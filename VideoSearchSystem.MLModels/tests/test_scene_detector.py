import unittest
from neural_models.dcnn_scene_detector.scene_detector import create_scene_detector

class TestSceneDetector(unittest.TestCase):
    def test_scene_detector_creation(self):
        model = create_scene_detector()
        self.assertIsNotNone(model)

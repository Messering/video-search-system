import numpy as np

from data_processing.video_loader import VideoLoader
from data_processing.rgb_to_hsv_converter import RGBToHSVConverter
from neural_models.dcnn_scene_detector.scene_detector import create_scene_detector
from feature_extraction.temporal_features import extract_temporal_features
from feature_extraction.spatial_features import extract_spatial_features
from feature_extraction.object_features import ObjectFeaturesExtractor
from integration.feature_integrator import integrate_features
from utils.helpers import ensure_dir
from storage.mongo_connector import MongoConnector
from config.config import VIDEO_DIR, OUTPUT_DIR
from utils.helpers import current_timestamp

def main(video_file):
    ensure_dir(OUTPUT_DIR)
    
    print(f"Processing video: {video_file}")
    video_loader = VideoLoader(VIDEO_DIR)
    frames = video_loader.extract_frames(video_file)

    print(f"Extracted {len(frames)} frames from {video_file}")

    temporal_features = extract_temporal_features(frames)

    spatial_features_list = []
    object_features_list = []

    object_feature_extractor = ObjectFeaturesExtractor()

    for idx, frame in enumerate(frames):
        spatial_feat = extract_spatial_features(frame)
        spatial_features_list.append(spatial_feat)

        object_feat = object_feature_extractor.extract_features(frame)
        object_features_list.append(object_feat)

    # Calculate average spatial and object features across all frames
    spatial_features = np.mean(spatial_features_list, axis=0)
    object_features = np.mean(object_features_list, axis=0)

    integral_vector = integrate_features(
        temporal_features, 
        spatial_features, 
        object_features
    )

    db_connector = MongoConnector()
    result = db_connector.insert_scene_data('scenes', {
        "video_id": video_file,
        "features": integral_vector.tolist(),
        "created_at": current_timestamp()
    })

    print(f"Data successfully stored to MongoDB with ID: {result.inserted_id}")

if __name__ == '__main__':
    ensure_dir(OUTPUT_DIR)
    video_file = "example.mp4"  # replace with your actual video file
    main(video_file)

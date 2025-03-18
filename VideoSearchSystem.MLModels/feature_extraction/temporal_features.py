import numpy as np

def extract_temporal_features(frames_hsv):
    mean_colors = np.mean(frames_hsv, axis=(0, 1, 2))
    std_colors = np.std(frames_hsv, axis=(0, 1, 2))
    temporal_features = np.concatenate([mean_colors, std_colors])
    return temporal_features

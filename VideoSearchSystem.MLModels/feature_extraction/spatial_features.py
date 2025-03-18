import numpy as np

def extract_spatial_features(frame_hsv):
    mean_colors = np.mean(frame_hsv, axis=(0, 1))
    std_colors = np.std(frame_hsv, axis=(0, 1))
    spatial_features = np.concatenate([mean_colors, std_colors])
    return spatial_features

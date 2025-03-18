import numpy as np

def integrate_features(temporal, spatial, object_features, weights=[0.4, 0.3, 0.3]):
    temporal, spatial, object_features = map(np.array, [temporal, spatial, object_features])
    
    integrated_vector = np.concatenate([
        temporal * weights[0],
        spatial * weights[1],
        object_features * weights[2]
    ])
    return integrated_vector

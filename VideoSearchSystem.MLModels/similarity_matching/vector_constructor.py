import numpy as np
from integration.feature_integrator import integrate_features

class VectorConstructor:
    def __init__(self, weights=[0.4, 0.3, 0.3]):
        self.weights = weights

    def construct_integral_vector(self, temporal_features, spatial_features, object_features):
        integral_vector = integrate_features(temporal, spatial, object_features, self.weights)
        return integral_vector

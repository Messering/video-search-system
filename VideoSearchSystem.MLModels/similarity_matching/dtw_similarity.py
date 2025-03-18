from scipy.spatial.distance import cdist
from scipy.signal import dtw

def compute_dtw_similarity(seq1, seq2):
    dist_matrix = cdist(seq1, seq2, metric='euclidean')
    alignment = dtw(dist_matrix)
    distance = alignment.normalizedDistance
    similarity = 1 / (1 + distance)
    return similarity

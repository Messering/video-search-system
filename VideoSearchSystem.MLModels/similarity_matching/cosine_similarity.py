from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(vec1, vec2):
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return similarity

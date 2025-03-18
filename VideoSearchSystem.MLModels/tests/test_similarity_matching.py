import unittest
import numpy as np
from similarity_matching.dtw_similarity import compute_dtw_similarity

class TestSimilarityMatching(unittest.TestCase):
    def test_dtw_similarity(self):
        seq1 = np.random.rand(10, 128)
        seq2 = np.random.rand(15, 128)
        sim = compute_dtw_similarity(seq1, seq2)
        self.assertTrue(0 <= sim <= 1)

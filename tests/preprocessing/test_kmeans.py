import numpy as np
from unittest import TestCase

from simulai.models import KMeansWrapper

class TestReshaper(TestCase):
    def setUp(self) -> None:
        pass

    def test_kmeans(self):

        n_clusters = 5

        data = np.random.rand(1_000, 3)

        kmeans = KMeansWrapper(n_clusters=n_clusters)

        kmeans.fit(input_data=data)

        clusters = kmeans.eval(input_data=data)

        assert isinstance(clusters, np.ndarray)

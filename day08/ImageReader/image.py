from typing import Tuple
from operator import mul
import numpy as np


class ImageReader:
    def __init__(self, image: str, dims: Tuple[int, int]):
        self.raw_image = [int(val) for val in str(image)]
        self.dims = dims
        self.image = np.reshape(self.raw_image, (-1, *dims))

    @property
    def check(self):
        least_zeros_layer = np.argmin([(layer == 0).sum() for layer in self.image])
        return mul(*[(self.image[least_zeros_layer] == i).sum() for i in range(1, 3)])

from typing import Tuple
from operator import mul
import numpy as np


class ImageReader:
    def __init__(self, image: str, dims: Tuple[int, int]):
        self.raw_image = [int(val) for val in str(image)]
        self.dims = dims
        self.layered_image = np.reshape(self.raw_image, (-1, *dims))

    @property
    def check(self):
        least_zeros_layer = np.argmin([(layer == 0).sum() for layer in self.layered_image])
        return mul(*[(self.layered_image[least_zeros_layer] == i).sum() for i in range(1, 3)])

    @staticmethod
    def visible_pixel_layer(pixels):
        return np.argmax(pixels != 2)

    @property
    def image(self):
        layer_ixs = np.apply_along_axis(self.visible_pixel_layer, 0, self.layered_image)
        output = np.zeros_like(layer_ixs)
        for i, rw in enumerate(layer_ixs):
            for j, val in enumerate(rw):
                output[i, j] = self.layered_image[val, i, j]
        return output

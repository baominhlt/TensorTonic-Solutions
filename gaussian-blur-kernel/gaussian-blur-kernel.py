import math
import numpy as np

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    x = np.arange(size) - size // 2
    y = (np.arange(size) - size // 2).reshape(-1, 1)

    g = np.exp(-(np.pow(x, 2) + np.pow(y, 2)) / (2 * np.pow(sigma, 2)))
    g = g / np.sum(g)
    return g.tolist()
    
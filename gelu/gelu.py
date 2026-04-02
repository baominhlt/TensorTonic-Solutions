import numpy as np
import math

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = to_array(x)
    x_shape = x.shape
    erf = to_array(list(map(lambda v: math.erf(v / math.sqrt(2)), x.reshape(-1)))).reshape(*x_shape)
    output = x / 2 * ( 1 + erf )
    return output

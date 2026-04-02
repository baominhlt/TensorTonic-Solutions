import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = to_array(x)
    return np.divide(np.exp(x) - np.exp(-x), np.exp(x) + np.exp(-x))
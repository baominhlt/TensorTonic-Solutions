import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = to_array(x)
    return np.where(x >= 0, x, 0)
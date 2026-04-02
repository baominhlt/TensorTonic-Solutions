import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = to_array(x)
    return np.where(x > 0, x, alpha * (np.exp(x) - 1)).tolist()
import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = to_array(x)
    y = to_array(y)
    
    return np.sqrt(np.sum(np.power(x - y, 2)))
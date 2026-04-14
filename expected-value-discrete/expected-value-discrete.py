import numpy as np


def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x


def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    p = to_array(p)
    if np.sum(p) != 1.0:
        raise ValueError
        
    x = to_array(x)
    return np.sum(x * p)

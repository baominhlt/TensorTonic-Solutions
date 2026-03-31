import numpy as np
from numpy.linalg import norm

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v)
    if len(v.shape) == 1:
        v_norm = norm(v)
    else:
        v_norm = norm(v, axis=1).reshape(-1, 1)
    v_norm = np.where(v_norm > 0, v_norm, 1e-8)
    return np.divide(v, v_norm)
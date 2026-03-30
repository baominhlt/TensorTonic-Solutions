import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    w = to_array(w)
    g = to_array(g)
    s = to_array(s)

    s_t = beta * s + (1 - beta) * np.power(g, 2)
    w_t = w - lr / (np.sqrt(s_t + eps)) * g
    return w_t, s_t
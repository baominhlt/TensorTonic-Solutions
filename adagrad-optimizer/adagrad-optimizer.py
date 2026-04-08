import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x


def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w = to_array(w)
    g = to_array(g)
    G = to_array(G)

    G_t = G + np.power(g, 2)
    return w - lr / np.sqrt(G_t + eps) * g, G_t
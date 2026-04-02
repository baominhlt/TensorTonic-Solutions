import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    x_t = to_array(x_t)
    h_prev = to_array(h_prev)
    Wx = to_array(Wx)
    Wh = to_array(Wh)
    b = to_array(b)
    return np.tanh(x_t @ Wx + h_prev @ Wh + b)

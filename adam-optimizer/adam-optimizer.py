import numpy as np

def to_array(x):
    if not isinstance(x, np.ndarray):
        return np.array(x)
    return x

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = to_array(param)
    grad = to_array(grad)
    m = to_array(m)
    v = to_array(v)

    m_t = beta1 * m + (1 - beta1) * grad
    v_t = beta2 * v + (1 - beta2) * np.power(grad, 2)
    m_bias = m_t / (1 - beta1 ** t)
    v_bias = v_t / (1 - beta2 ** t)
    updated_param = param - lr * (m_bias / (np.sqrt(v_bias) + eps))
    return updated_param, m_t, v_t
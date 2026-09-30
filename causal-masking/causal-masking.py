import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    scores = np.array(scores)
    seq_len_i, seq_len_j = scores.shape[-2:]

    i = np.arange(seq_len_i).reshape(-1, 1)
    j = np.arange(seq_len_j).reshape(1, -1)
    causal_bool_mask = i >= j

    return np.where(causal_bool_mask, scores, mask_value)
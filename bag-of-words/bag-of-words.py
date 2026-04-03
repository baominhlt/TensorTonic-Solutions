import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    if len(vocab) == 0:
        return np.array([], dtype=int)
    return np.array([tokens.count(token) for token in vocab], dtype=int)
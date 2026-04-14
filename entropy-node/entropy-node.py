import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if not isinstance(y, np.ndarray):
        y = np.array(y)
        
    num_samples = y.shape[0]
    labels, counts = np.unique(y, return_counts=True)
    entropy = -1.0 * sum([counts[i] / num_samples * np.log2(counts[i] / num_samples) for i in range(len(counts))])
    return entropy
    
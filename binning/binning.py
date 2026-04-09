import math

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    if all([value == values[0] for value in values]):
        return [0] * len(values)
    
    min_values = min(values)
    w = (max(values) - min_values)/ num_bins
    return [math.floor(min((x - min_values) / w, num_bins - 1)) for x in values]

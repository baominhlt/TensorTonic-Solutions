import math
import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    pmf = np.exp(-lam) * np.power(lam, k) / math.factorial(k)
    cdf = np.sum([np.exp(-lam) * np.power(lam, i) / math.factorial(i) for i in range(k + 1)])
    return pmf, cdf
    
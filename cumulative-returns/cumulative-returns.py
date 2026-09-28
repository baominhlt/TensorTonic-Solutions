def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    w_t_1 = 1.0
    output = []

    for cumulative_return in returns:
        w_t = w_t_1 * (1 + cumulative_return)
        R_t = w_t - 1
        output.append(R_t)
        w_t_1 = w_t
    return output
        
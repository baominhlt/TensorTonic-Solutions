def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = a * (x0 ** 2) + b * x0 + c
    for _ in range(steps):
        x -= lr * (2 * a * x + b)
    return x
    
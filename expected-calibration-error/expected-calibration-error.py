def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    num_samples = len(y_true)
    bin_width = 1 / n_bins

    ece = 0
    for idx in range(n_bins):
        left, right = bin_width * idx, bin_width * (idx + 1)
        if right == 1:
            right += 1e-8  # Make sure 1.0 confidence score is included in the last bin
        ids_in_bin = [j for j in range(num_samples) if y_pred[j] >= left and y_pred[j] < right]
        if len(ids_in_bin) == 0:
            continue

        acc = 1 / len(ids_in_bin) * sum([y_true[j] for j in ids_in_bin])
        conf = 1 / len(ids_in_bin) * sum([y_pred[j] for j in ids_in_bin])
        ece += len(ids_in_bin) / num_samples * abs(acc - conf)

    return ece
    
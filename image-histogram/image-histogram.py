def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    outputs = [0] * 256
    for dim in image:
        for pixel in dim:
            outputs[pixel] += 1
    return outputs
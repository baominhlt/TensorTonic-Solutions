import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    is_1d_array = False
    if not isinstance(points[0], list):
        points = [points]
        is_1d_array = True

    outputs = []
    for point in points:
        output = []
        for i in range(len(T) - 1):
            T_i = sum([T[i][j] * point[j] for j in range(len(point))]) + T[i][-1]
            output.append(T_i)
        outputs.append(output)

    if is_1d_array:
        return outputs[0]
    return outputs